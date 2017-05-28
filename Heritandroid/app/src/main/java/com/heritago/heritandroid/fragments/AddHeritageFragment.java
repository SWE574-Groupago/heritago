package com.heritago.heritandroid.fragments;

import android.Manifest;
import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.media.ExifInterface;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.app.Fragment;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Toast;

import com.heritago.heritandroid.MainActivity;
import com.heritago.heritandroid.R;
import com.heritago.heritandroid.adapters.AddHeritageDetailAdapter;
import com.heritago.heritandroid.adapters.HeritageAdapter;
import com.heritago.heritandroid.adapters.HeritageMultimediaAdapter;
import com.heritago.heritandroid.api.ApiClient;
import com.heritago.heritandroid.api.ApiInterface;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidRemoveHeritageDetailItemEvent;
import com.heritago.heritandroid.model.Heritage;
import com.squareup.otto.Subscribe;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * Created by onurtokoglu on 30/03/2017.
 */

public class AddHeritageFragment extends Fragment {
    private static final String TAG = "Add";
    private static final int CAMERA_PERMISSION_CODE = 1;
    private static final int CAMERA_REQUEST_CODE = 1;

    private ListView mListView;
    private AddHeritageDetailAdapter adapter;
    private ArrayList<Heritage.BasicInformation> detailList;
    private ArrayList<Heritage.Multimedia> multimediaList;
    private RecyclerView recyclerView;
    private HeritageMultimediaAdapter multimediaAdapter;

    private EditText title_text;
    private EditText description_text;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public void onResume() {
        super.onResume();
        BusProvider.getInstance().register(this);
    }

    @Override
    public void onPause() {
        super.onPause();
        BusProvider.getInstance().unregister(this);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_add_heritage, container, false);

        detailList = new ArrayList<>();
        adapter = new AddHeritageDetailAdapter(detailList);
        mListView = (ListView) view.findViewById(R.id.heritage_detail_list);
        mListView.setAdapter(adapter);

        Button addButton = (Button) view.findViewById(R.id.add_button);
        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                detailList.add(new Heritage.BasicInformation("",""));
                adapter.notifyDataSetChanged();
                resizeDetailListView();
            }
        });

        ImageButton camera = (ImageButton) view.findViewById(R.id.camera_button);
        camera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openCamera();
            }
        });

        multimediaList = new ArrayList<>();
        multimediaAdapter = new HeritageMultimediaAdapter(multimediaList);
        recyclerView = (RecyclerView) view.findViewById(R.id.recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        recyclerView.setAdapter(multimediaAdapter);

        Button sendButton = (Button) view.findViewById(R.id.save_button);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                postHeritage();
            }
        });

        title_text = (EditText) view.findViewById(R.id.title);
        description_text = (EditText) view.findViewById(R.id.description);

        return view;
    }

    @Subscribe public void didRemoveHeritageDetailItemEvent(DidRemoveHeritageDetailItemEvent event){
        resizeDetailListView();
    }

    private void resizeDetailListView(){
        Log.d("List",detailList.size()+"");
        if (mListView.getChildCount() > 0){
            int height = mListView.getChildAt(0).getHeight();
            if (mListView.getCount() > 0){
                mListView.setLayoutParams(new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, height*mListView.getCount()));
            }
        }
    }

    private void openCamera(){
        Toast.makeText(getActivity(), "Open camera", Toast.LENGTH_SHORT).show();
        if (ContextCompat.checkSelfPermission(getActivity(), Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED){
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                requestPermissions(new String[]{Manifest.permission.CAMERA}, CAMERA_PERMISSION_CODE);
            }
        }else{
            Intent intent = new Intent("android.media.action.IMAGE_CAPTURE");
            startActivityForResult(intent, CAMERA_REQUEST_CODE);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if (requestCode == CAMERA_PERMISSION_CODE){
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED){
                Toast.makeText(getActivity(), "Permission granted", Toast.LENGTH_SHORT).show();
                openCamera();
            }else{
                Toast.makeText(getActivity(), "Permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == CAMERA_REQUEST_CODE && resultCode == Activity.RESULT_OK){
            Toast.makeText(getActivity(), "Activity Result", Toast.LENGTH_SHORT).show();
            Bitmap photo = (Bitmap) data.getExtras().get("data");
            //rotate 90 deg
            Matrix matrix = new Matrix();
            matrix.postRotate(90f);
            photo = Bitmap.createBitmap(photo, 0, 0, photo.getWidth(), photo.getHeight(), matrix, true);

            Heritage.Multimedia image = new Heritage.Multimedia(Heritage.Multimedia.Type.image);
            multimediaList.add(image);
            multimediaAdapter.addBitmap(multimediaList.size()-1, photo);
            multimediaAdapter.notifyDataSetChanged();
        }else{
            super.onActivityResult(requestCode, resultCode, data);
        }
    }


    public void postHeritage(){
        String title = title_text.getText().toString();
        String description = description_text.getText().toString();

        if (title.equals("") || description.equals("")){
            return;
        }

        Heritage heritage = new Heritage("na", title, description, new Heritage.Owner("s", "Suzan U."));
        for (Heritage.BasicInformation b: detailList){
            if (!b.name.equals("") && !b.value.equals("")){
                heritage.getBasicInformation().add(b);
            }
        }


        ApiInterface inter = ApiClient.getClient().create(ApiInterface.class);
        Call call = inter.postHeritage(heritage);
        call.enqueue(new Callback() {
            @Override
            public void onResponse(Call call, Response response) {
                Log.d(TAG, "api call success: "+call.request().url());
                Heritage createdHeritage;
                try {
                    createdHeritage = (Heritage) response.body();
                }catch (Exception e){
                    Log.d(TAG, "heritage create response cast error "+e.getMessage());
                    return;
                }
                Log.d(TAG, "created heritage id "+createdHeritage.id);
                for (Integer i: multimediaAdapter.getBitmaps().keySet()){
                    postMultimedia(createdHeritage.id,multimediaAdapter.getBitmaps().get(i), Heritage.Multimedia.Type.image);
                }

                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                    }
                }).setTitle("Success").setMessage("Heritage item successfully created.");
                builder.create().show();
            }

            @Override
            public void onFailure(Call call, Throwable t) {
                Log.d(TAG, "fail "+t.getMessage());
            }
        });
    }

    public void postMultimedia(String heritageId, Bitmap bitmap, Heritage.Multimedia.Type type){
        ApiInterface inter = ApiClient.getClient().create(ApiInterface.class);

        String fileName = Double.toString(Math.random());
        File file = new File(getActivity().getCacheDir(),fileName);
        OutputStream os;
        try {
            os = new BufferedOutputStream(new FileOutputStream(file));
            bitmap.compress(Bitmap.CompressFormat.JPEG, 100, os);
            os.close();
        } catch (Exception e) {
            e.printStackTrace();
            Log.d(TAG, "bitmap to file convert error "+e.getMessage());
            return;
        }


        RequestBody reqFile = RequestBody.create(MediaType.parse("image/*"), file);
        MultipartBody.Part body = MultipartBody.Part.createFormData("file", file.getName(), reqFile);
        RequestBody type_field = RequestBody.create(MediaType.parse("text/plain"), type.name());

        Call call = inter.postMultimedia(heritageId, body, type_field);
        call.enqueue(new Callback() {
            @Override
            public void onResponse(Call call, Response response) {
                Log.d(TAG, "multimedia upload response code "+response.code()+" "+call.request().url());
                Log.d(TAG, "multimedia upload response message "+response.message());
            }

            @Override
            public void onFailure(Call call, Throwable t) {
                Log.d(TAG, "multimedia upload failed "+t.getMessage());
            }
        });
    }

}

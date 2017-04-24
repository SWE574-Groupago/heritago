package com.heritago.heritandroid.fragments;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.app.Fragment;
import android.support.v4.content.ContextCompat;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Toast;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.adapters.AddHeritageDetailAdapter;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidRemoveHeritageDetailItemEvent;
import com.heritago.heritandroid.model.HeritageDetail;
import com.squareup.otto.Subscribe;

import java.util.ArrayList;

/**
 * Created by onurtokoglu on 30/03/2017.
 */

public class AddHeritageFragment extends Fragment {
    private static final int CAMERA_PERMISSION_CODE = 1;
    private static final int CAMERA_REQUEST_CODE = 1;

    private ListView mListView;
    private AddHeritageDetailAdapter adapter;
    private ArrayList<HeritageDetail> detailList;

    private ImageButton locationButton;

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
                detailList.add(new HeritageDetail());
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

        locationButton = (ImageButton) view.findViewById(R.id.location_button);

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
            locationButton.setImageBitmap(photo);
        }else{
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}

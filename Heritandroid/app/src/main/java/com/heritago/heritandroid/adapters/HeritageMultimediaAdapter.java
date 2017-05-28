package com.heritago.heritandroid.adapters;

import android.graphics.Bitmap;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidTapHeritageCardEvent;
import com.heritago.heritandroid.model.Heritage;
import com.nostra13.universalimageloader.core.ImageLoader;

import java.util.HashMap;
import java.util.List;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class HeritageMultimediaAdapter extends RecyclerView.Adapter<HeritageMultimediaAdapter.MultimediaViewHolder> {
    static private final String TAG = "Adapter";

    private List<Heritage.Multimedia> multimediaList;
    private HashMap<Integer, Bitmap> bitmaps;

    public class MultimediaViewHolder extends RecyclerView.ViewHolder {
        public ImageView image;

        public MultimediaViewHolder(View view) {
            super(view);
            image = (ImageView) view.findViewById(R.id.card_image);
        }
    }

    public HeritageMultimediaAdapter(List<Heritage.Multimedia> multimediaList) {
        this.multimediaList = multimediaList;
        this.bitmaps = new HashMap<>();
    }

    public void addBitmap(int position, Bitmap map){
        bitmaps.put(position, map);
    }

    public HashMap<Integer, Bitmap> getBitmaps(){
        return bitmaps;
    }

    @Override
    public MultimediaViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.card_multimedia, parent, false);
        return new MultimediaViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(MultimediaViewHolder holder, int position) {
        final Heritage.Multimedia multimedia = multimediaList.get(position);
        switch (multimedia.getType()){
            case image:
                if (multimedia.getUrl() != null){
                    ImageLoader.getInstance().displayImage(multimedia.getUrl(), holder.image);
                }else if (bitmaps.get(position) != null){
                    holder.image.setImageBitmap(bitmaps.get(position));
                }
        }
    }

    @Override
    public int getItemCount() {
        return multimediaList.size();
    }

    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
    }

}

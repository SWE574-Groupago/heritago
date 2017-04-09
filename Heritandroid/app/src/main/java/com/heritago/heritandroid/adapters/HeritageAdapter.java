package com.heritago.heritandroid.adapters;

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
import com.nostra13.universalimageloader.core.assist.ImageScaleType;

import java.util.List;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class HeritageAdapter extends RecyclerView.Adapter<HeritageAdapter.HeritageViewHolder> {

    private List<Heritage> heritageList;

    public class HeritageViewHolder extends RecyclerView.ViewHolder {
        public TextView title;
        public TextView creator;
        public ImageView image;

        public HeritageViewHolder(View view) {
            super(view);
            title = (TextView) view.findViewById(R.id.card_title);
            creator = (TextView) view.findViewById(R.id.card_creator);
            image = (ImageView) view.findViewById(R.id.card_image);
        }
    }

    public HeritageAdapter(List<Heritage> heritageList) {
        this.heritageList = heritageList;
    }


    @Override
    public HeritageViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.card_heritage, parent, false);
        return new HeritageViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(HeritageViewHolder holder, int position) {
        final Heritage heritage = heritageList.get(position);
        holder.title.setText(heritage.getTitle());
        holder.creator.setText(heritage.getCreator());
        ImageLoader.getInstance().displayImage(heritage.imageUrl, holder.image);
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d("Adapter", "Holder clicked");
                BusProvider.getInstance().post(new DidTapHeritageCardEvent(heritage));
            }
        });
    }

    @Override
    public int getItemCount() {
        return heritageList.size();
    }

    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
    }

}

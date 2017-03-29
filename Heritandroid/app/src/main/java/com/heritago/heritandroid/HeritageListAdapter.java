package com.heritago.heritandroid;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by onurtokoglu on 29/03/2017.
 */

public class HeritageListAdapter extends BaseAdapter {
    private Context mContext;
    private LayoutInflater mInflater;
    private ArrayList<Heritage> mDataSource;

    public HeritageListAdapter(Context context, ArrayList<Heritage> heritages){
        mContext = context;
        mDataSource = heritages;
        mInflater = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    @Override
    public int getCount() {
        return mDataSource.size();
    }

    @Override
    public Object getItem(int position) {
        return mDataSource.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder;

        if(convertView == null) {
            convertView = mInflater.inflate(R.layout.list_item_heritage, parent, false);

            holder = new ViewHolder();
            holder.titleTextView = (TextView) convertView.findViewById(R.id.titleText);
            holder.creatorTextView = (TextView) convertView.findViewById(R.id.creatorText);
            holder.image1 = (ImageView) convertView.findViewById(R.id.image1);
            holder.image2 = (ImageView) convertView.findViewById(R.id.image2);
            holder.image3 = (ImageView) convertView.findViewById(R.id.image3);

            convertView.setTag(holder);
        }
        else{
            holder = (ViewHolder) convertView.getTag();
        }

        Heritage heritage = (Heritage) getItem(position);

        holder.titleTextView.setText(heritage.title);
        holder.creatorTextView.setText(heritage.creator);

        return convertView;
    }
    private static class ViewHolder {
        public TextView titleTextView;
        public TextView creatorTextView;
        public ImageView image1;
        public ImageView image2;
        public ImageView image3;
    }

}

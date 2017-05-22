package com.heritago.heritandroid.fragments;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.TextView;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.model.Heritage;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class HeritageDetailFragment extends Fragment {
    private Heritage heritage;

    public void setHeritage(Heritage heritage) {
        this.heritage = heritage;
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_heritage_detail, container, false);

        TextView title = (TextView) view.findViewById(R.id.title);
        title.setText(heritage.getTitle());

        TextView description = (TextView) view.findViewById(R.id.description);
        description.setText(heritage.getDescription());

        ListView heritageDetailList = (ListView) view.findViewById(R.id.heritage_detail_list);
        DetailAdapter detailAdapter = new DetailAdapter(heritage.getBasicInformation());
        heritageDetailList.setAdapter(detailAdapter);

        return view;
    }


    private class DetailAdapter extends BaseAdapter {
        private List<Heritage.BasicInformation> detailList;

        public DetailAdapter(List<Heritage.BasicInformation> detailList) {
            this.detailList = detailList;
        }

        @Override
        public int getCount() {
            return detailList.size();
        }

        @Override
        public Object getItem(int position) {
            return detailList.get(position);
        }

        @Override
        public long getItemId(int position) {
            return position;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_heritage_detail_list, parent, false);

            TextView key = (TextView) view.findViewById(R.id.key_text);
            key.setText(detailList.get(position).name);

            TextView value = (TextView) view.findViewById(R.id.value_text);
            value.setText(detailList.get(position).value);

            return view;
        }
    }
}

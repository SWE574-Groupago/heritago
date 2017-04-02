package com.heritago.heritandroid.fragments;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.model.Heritage;

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

        return view;
    }


}

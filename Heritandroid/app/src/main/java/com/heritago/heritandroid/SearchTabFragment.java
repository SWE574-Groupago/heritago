package com.heritago.heritandroid;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ListView;

import java.util.ArrayList;


public class SearchTabFragment extends Fragment {
    private ListView mListView;
    private HeritageListAdapter mAdapter;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_tab_search, container, false);
        mListView = (ListView) view.findViewById(R.id.heritage_list_view);
        final ArrayList<Heritage> heritages = new ArrayList<>();
        for (int i = 0; i < 5; i++){
            Heritage her = new Heritage("");
            her.title = "asdasda";
            her.creator = "qweqweqwe";
            heritages.add(her);
        }

        mAdapter = new HeritageListAdapter(getContext(), heritages);
        mListView.setAdapter(mAdapter);

        mListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Heritage selected = heritages.get(position);
                Intent detail = new Intent(getContext(), HeritageDetailActivity.class);
                detail.putExtra("heritage", selected.id);
                startActivityForResult(detail, 0);
            }
        });

        return view;
    }





}

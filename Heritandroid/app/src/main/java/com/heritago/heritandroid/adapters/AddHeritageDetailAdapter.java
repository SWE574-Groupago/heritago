package com.heritago.heritandroid.adapters;

import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.EditText;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidRemoveHeritageDetailItemEvent;
import com.heritago.heritandroid.model.Heritage;

import java.util.ArrayList;



public class AddHeritageDetailAdapter extends BaseAdapter {
    private ArrayList<Heritage.BasicInformation> detailList;

    public AddHeritageDetailAdapter(ArrayList<Heritage.BasicInformation> detailList) {
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
    public View getView(final int position, View convertView, ViewGroup parent) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_add_heritage_detail_list, parent, false);
        Button button = (Button) view.findViewById(R.id.delete_button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                detailList.remove(position);
                notifyDataSetChanged();
                BusProvider.getInstance().post(new DidRemoveHeritageDetailItemEvent());
            }
        });

        EditText keyText = (EditText) view.findViewById(R.id.key_text);
        keyText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                detailList.get(position).key = s.toString();
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        EditText valueText = (EditText) view.findViewById(R.id.value_text);
        valueText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                detailList.get(position).value = s.toString();
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        return view;
    }



}

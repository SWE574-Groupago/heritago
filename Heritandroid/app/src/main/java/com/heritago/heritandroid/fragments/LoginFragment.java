package com.heritago.heritandroid.fragments;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import com.heritago.heritandroid.R;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidLoginEvent;


import static android.content.Context.INPUT_METHOD_SERVICE;

/**
 * Created by onurtokoglu on 14/05/2017.
 */

public class LoginFragment extends Fragment {

    EditText username_field;
    EditText password_field;
    Button login_button;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_login, container, false);

        username_field = (EditText) view.findViewById(R.id.username);
        password_field = (EditText) view.findViewById(R.id.password);
        login_button = (Button) view.findViewById(R.id.login_button);
        login_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                loginClicked();
            }
        });

        return view;
    }

    public void loginClicked(){
        String username = username_field.getText().toString();
        String password = password_field.getText().toString();
        if (username.equals("") || password.equals("")){
            return;
        }

        //TODO: check login

        InputMethodManager imm = (InputMethodManager) getActivity().getSystemService(INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(getActivity().getCurrentFocus().getWindowToken(), 0);
        BusProvider.getInstance().post(new DidLoginEvent());
    }






}

package com.heritago.heritandroid.fragments;

import android.app.Fragment;
import android.app.FragmentManager;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.SearchView;

import com.heritago.heritandroid.R;
import com.heritago.heritandroid.adapters.HeritageAdapter;
import com.heritago.heritandroid.bus.BusProvider;
import com.heritago.heritandroid.bus.DidLoginEvent;
import com.heritago.heritandroid.helpers.LoginHelper;
import com.squareup.otto.Subscribe;

/**
 * Created by onurtokoglu on 14/05/2017.
 */

public class ProfileFragment extends Fragment {

    LinearLayout masterLinear;

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
        View view = inflater.inflate(R.layout.fragment_profile, container, false);

        masterLinear = (LinearLayout) view.findViewById(R.id.master_linear);

        if(LoginHelper.shared.isLoggedIn()) {
            addSearchFragment();
        }else{
            Fragment lf = new LoginFragment();
            getFragmentManager().beginTransaction().addToBackStack(null)
                    .add(R.id.master_linear, lf, "login").commit();
        }

        return view;
    }

    private void addSearchFragment(){
        SearchFragment sf = new SearchFragment();
        sf.parentIsProfile = true;
        getFragmentManager().beginTransaction().add(R.id.master_linear, sf).commit();
    }

    @Subscribe
    public void didLogin(DidLoginEvent event){
        Fragment lf = getFragmentManager().findFragmentByTag("login");
        if(lf!=null) getFragmentManager().beginTransaction().remove(lf).commit();
        addSearchFragment();
    }


}

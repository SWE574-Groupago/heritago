package com.heritago.heritandroid.api;

import com.heritago.heritandroid.model.Heritage;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by onurtokoglu on 16/04/2017.
 */

public interface ApiInterface {

    @GET("heritages")
    Call<List<Heritage>> getHeritages(
            @Query("q") String query,
            @Query("user") String username);



}

package com.heritago.heritandroid.api;


import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ApiClient {
    public static final String imageBaseUrl = "http://54.154.214.100/api/v1";
    private static final String baseUrl = "http://54.154.214.100/api/v1/"; //"http://10.0.2.2:8000";
    private static Retrofit retrofit;

    public static Retrofit getClient(){
        if (retrofit != null) return retrofit;

        OkHttpClient client = new OkHttpClient.Builder().build();

        retrofit = new Retrofit.Builder()
                .baseUrl(baseUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .client(client)
                .build();

        return retrofit;
    }




}

package com.heritago.heritandroid.api;


import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ApiClient {
    public static final String imageBaseUrl = "http://54.154.214.100/api/v1";
    private static final String baseUrl = "http://54.154.214.100/api/v1/"; //"http://10.0.2.2:8000/api/v1/";
    private static Retrofit retrofit;

    public static Retrofit getClient(){
        if (retrofit != null) return retrofit;

        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        logging.setLevel(HttpLoggingInterceptor.Level.BODY);

        OkHttpClient client = new OkHttpClient.Builder()
                .addInterceptor(logging).build();

        retrofit = new Retrofit.Builder()
                .baseUrl(baseUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .client(client)
                .build();

        return retrofit;
    }




}

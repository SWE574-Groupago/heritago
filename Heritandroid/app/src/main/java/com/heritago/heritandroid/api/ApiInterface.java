package com.heritago.heritandroid.api;

import com.heritago.heritandroid.model.Heritage;

import java.util.HashMap;
import java.util.List;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Path;
import retrofit2.http.Query;

/**
 * Created by onurtokoglu on 16/04/2017.
 */

public interface ApiInterface {

    @GET("heritages")
    Call<List<Heritage>> getHeritages(
            @Query("q") String query,
            @Query("user") String username);


    @POST("heritages/")
    Call<Heritage> postHeritage(@Body Heritage heritage);

    @Multipart
    @POST("heritages/{heritageId}/multimedia")
    Call<ResponseBody> postMultimedia(@Path("heritageId") String HeritageId, @Part MultipartBody.Part image, @Part("type") RequestBody type);
}

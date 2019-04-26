package com.mab.gymtrainer;

import retrofit2.Call;
import retrofit2.http.GET;

public interface ApiService {
    @GET("one")
    Call<Message> getOne();

    @GET("two")
    Call<Message> getTwo();

}

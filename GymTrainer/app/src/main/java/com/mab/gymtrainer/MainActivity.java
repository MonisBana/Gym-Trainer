package com.mab.gymtrainer;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.CardView;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {
    private EditText IpField;
    private Button IpBtn;
    private CardView OneBtn,TwoBtn;
    private ApiService mApiService;
    private String IpAddress ="http://192.168.0.100:5000/";
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        IpField = findViewById(R.id.ipField);
        IpBtn = findViewById(R.id.ipBtn);
        OneBtn = findViewById(R.id.oneBtn);
        TwoBtn = findViewById(R.id.twoBtn);
        Retrofit.Builder builder = new Retrofit.Builder()
                .baseUrl(IpAddress)
                .addConverterFactory(GsonConverterFactory.create());
        Retrofit retrofit = builder.build();
        mApiService = retrofit.create(ApiService.class);
        IpField.setText("http://192.168.0.102:5000/");
        IpBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                IpAddress = IpField.getText().toString();
                Retrofit.Builder builder = new Retrofit.Builder()
                        .baseUrl(IpAddress)
                        .addConverterFactory(GsonConverterFactory.create());
                Retrofit retrofit = builder.build();
                mApiService = retrofit.create(ApiService.class);
                IpField.setVisibility(View.GONE);
                IpBtn.setVisibility(View.GONE);
                Toast.makeText(MainActivity.this, "Connected", Toast.LENGTH_SHORT).show();
            }
        });
        OneBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mApiService.getOne().enqueue(new Callback<Message>() {
                    @Override
                    public void onResponse(Call<Message> call, Response<Message> response) {
                        if(response.isSuccessful())
                        Toast.makeText(MainActivity.this, response.body().getMsg(), Toast.LENGTH_SHORT).show();
                    }

                    @Override
                    public void onFailure(Call<Message> call, Throwable t) {
                        Toast.makeText(MainActivity.this, "Error"+t, Toast.LENGTH_SHORT).show();
                        Log.e("BAV","Error :"+t);
                    }
                });
            }
        });
        TwoBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                mApiService.getTwo().enqueue(new Callback<Message>() {
                    @Override
                    public void onResponse(Call<Message> call, Response<Message> response) {
                        if(response.isSuccessful())
                            Toast.makeText(MainActivity.this, response.body().getMsg(), Toast.LENGTH_SHORT).show();
                    }

                    @Override
                    public void onFailure(Call<Message> call, Throwable t) {
                        Toast.makeText(MainActivity.this, "Error"+t, Toast.LENGTH_SHORT).show();
                        Log.e("BAV","Error :"+t);
                    }
                });
            }
        });

    }
}

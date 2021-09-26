package com.example.Order_System;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity {
    EditText cust_name, cust_id, cust_address;
    TextView result;
    Button submitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        cust_name = (EditText) findViewById(R.id.et_1);
        cust_id = (EditText) findViewById(R.id.et_2);
        cust_address = (EditText) findViewById(R.id.et_3);
        result = (TextView) findViewById(R.id.tv_4);
        submitButton = (Button) findViewById(R.id.b_1);
        submitButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                String id= cust_id.getText().toString();
                String name = cust_name.getText().toString();
                String address = cust_address.getText().toString();

                    if (Pattern.compile("[0-9]").matcher(name).find()) {
                        cust_name.setError("Customer name cannot contain numbers.");
                        cust_name.requestFocus();
                    } else if (cust_name.getText().toString().length() < 1) {
                        cust_name.setError("Customer Name is required.");
                        cust_name.requestFocus();
                    } else if (cust_name.getText().toString().trim().equals("")) {
                        cust_name.setError("Customer Name is required.");
                        cust_name.requestFocus();
                    } else if (cust_id.getText().toString().trim().length() < 1) {
                        cust_id.setError("Customer ID is required.");
                        cust_id.requestFocus();
                    } else if (cust_id.getText().toString().trim().equals("")) {
                        cust_id.setError("Customer ID is required.");
                        cust_id.requestFocus();
                    }  else if (cust_id.getText().toString().trim().length() > 1) {
                        int intid = Integer.parseInt(id);
                        if (intid < 0 || intid > 1000) {
                            cust_id.setError("Customer ID must be between 0 and 1000");
                            cust_id.requestFocus();
                        } else if (cust_address.getText().toString().trim().length() < 1) {
                            cust_address.setError("Customer Address is required.");
                            cust_address.requestFocus();
                        } else if (cust_address.getText().toString().trim().equals("")) {
                            cust_address.setError("Customer Address is required");
                            cust_address.requestFocus();
                        } else {openActivity2();}
                    }
            }
        });
    }
    public void openActivity2(){
        Intent intent = new Intent(this, Main2Activity.class);
        startActivity(intent);
    }
}
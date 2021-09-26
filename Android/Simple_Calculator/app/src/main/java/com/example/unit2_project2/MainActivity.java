package com.example.unit2_project2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button addbtn = (Button) findViewById(R.id.b1_add);
        Button subbtn = (Button) findViewById(R.id.b4_sub);
        Button multibtn = (Button) findViewById(R.id.b5_multi);
        Button divbtn = (Button) findViewById(R.id.b3_div);
        Button modbtn = (Button) findViewById(R.id.b2_mod);
        Button expbtn = (Button) findViewById(R.id.b6_exp);
        addbtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                int num1 = Integer.parseInt(first.getText().toString());
                int num2 = Integer.parseInt(second.getText().toString());
                int result = num1 + num2;
                textResult.setText("The sum of " + num1 + " and " + num2 + " is " + result + ".");
            }
        });

        subbtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                int num1 = Integer.parseInt(first.getText().toString());
                int num2 = Integer.parseInt(second.getText().toString());
                int result = num1 - num2;
                textResult.setText("The difference of " + num1 + " and " + num2 + " is " + result + ".");
            }
        });

        multibtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                int num1 = Integer.parseInt(first.getText().toString());
                int num2 = Integer.parseInt(second.getText().toString());
                int result = num1 * num2;
                textResult.setText("The product of " + num1 + " and " + num2 + " is " + result + ".");
            }
        });

        divbtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                Double num1 = Double.parseDouble(first.getText().toString());
                Double num2 = Double.parseDouble(second.getText().toString());
                Double result = num1 / num2;
                textResult.setText("The quotient of " + num1 + " and " + num2 + " is " + result + ".");
            }
        });

        modbtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                int num1 = Integer.parseInt(first.getText().toString());
                int num2 = Integer.parseInt(second.getText().toString());
                int result = num1 % num2;
                textResult.setText(num1 + " mod " + num2 + " equals " + result + ".");
            }
        });

        expbtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                EditText first = (EditText) findViewById(R.id.et_1);
                EditText second = (EditText) findViewById(R.id.et_2);
                TextView textResult = (TextView) findViewById(R.id.tv_1);

                Double num1 = Double.parseDouble(first.getText().toString());
                Double num2 = Double.parseDouble(second.getText().toString());
                Double result = Math.pow(num1,num2);
                textResult.setText(num1 + " raised to the power of " + num2 + " equals " + result);
            }
        });
    }
}

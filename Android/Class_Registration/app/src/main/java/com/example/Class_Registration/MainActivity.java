package com.example.Class_Registration;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import java.util.ArrayList;
import java.util.Collections;

public class MainActivity extends AppCompatActivity {

    Button reg_page_button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        reg_page_button = (Button) findViewById(R.id.next_page);
        reg_page_button.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                openActivity2();
            }
        });
        TextView class_1 = (TextView) findViewById(R.id.class_name_1);
        TextView class_2 = (TextView) findViewById(R.id.class_name_2);
        TextView class_3 = (TextView) findViewById(R.id.class_name_3);
        String not_registered = "Class not registered";
        try {
            ArrayList<String> classes = getIntent().getExtras().getStringArrayList("classes");

            if (classes.size() <= 0) {
                class_1.setText(not_registered);
                class_2.setText(not_registered);
                class_3.setText(not_registered);
            } else if (classes.size() == 1) {
                String class_new_1 = classes.get(0);
                class_1.setText(class_new_1);
                class_2.setText(not_registered);
                class_3.setText(not_registered);
            } else if (classes.size() == 2) {
                String class_new_1 = classes.get(0);
                String class_new_2 = classes.get(1);
                class_1.setText(class_new_1);
                class_2.setText(class_new_2);
                class_3.setText(not_registered);
            } else if (classes.size() == 3) {
                String class_new_1 = classes.get(0);
                String class_new_2 = classes.get(1);
                String class_new_3 = classes.get(2);
                class_1.setText(class_new_1);
                class_2.setText(class_new_2);
                class_3.setText(class_new_3);
            }
        } catch (Exception e) {
            class_1.setText(not_registered);
            class_2.setText(not_registered);
            class_3.setText(not_registered);
        }
    }

    public void openActivity2() {
        Intent intent = new Intent(this, Main2Activity.class);
        startActivity(intent);
    }

    public void onClickSubmit(View view) {
        EditText grade_1_et = (EditText) findViewById(R.id.grade_1);
        EditText grade_2_et = (EditText) findViewById(R.id.grade_2);
        EditText grade_3_et = (EditText) findViewById(R.id.grade_3);
        TextView class_3 = (TextView) findViewById(R.id.class_name_3);
        String not_registered = "Class not registered";

        if (class_3.getText() == not_registered) {
                grade_1_et.setError("You must register for three classes before calculating your grade.");
                grade_1_et.requestFocus();
        }
        else if (grade_1_et.getText().toString().trim().length() < 1) {
            grade_1_et.setError("Grade is required.");
            grade_1_et.requestFocus();
        }
        else if (grade_2_et.getText().toString().trim().length() < 1) {
            grade_2_et.setError("Grade is required.");
            grade_2_et.requestFocus();
        } else if (grade_3_et.getText().toString().trim().length() < 1) {
            grade_3_et.setError("Grade is required.");
            grade_3_et.requestFocus();
        } else {

            Float grade_1 = Float.parseFloat(grade_1_et.getText().toString());
            Float grade_2 = Float.parseFloat(grade_2_et.getText().toString());
            Float grade_3 = Float.parseFloat(grade_3_et.getText().toString());

            if (grade_1 < 0 || grade_1 > 100) {
                grade_1_et.setError("Grade must be between 0 and 100");
                grade_1_et.requestFocus();
            } else if (grade_2 < 0 || grade_2 > 100) {
                grade_2_et.setError("Grade must be between 0 and 100");
                grade_2_et.requestFocus();
            } else if (grade_3 < 0 || grade_3 > 100) {
                grade_3_et.setError("Grade must be between 0 and 100");
                grade_3_et.requestFocus();
            } else {

                ArrayList<Float> grades = new ArrayList<>();

                grades.add(grade_1);
                grades.add(grade_2);
                grades.add(grade_3);

                TextView letter_grade_1 = (TextView) findViewById(R.id.letter_grade_1);
                TextView letter_grade_2 = (TextView) findViewById(R.id.letter_grade_2);
                TextView letter_grade_3 = (TextView) findViewById(R.id.letter_grade_3);
                TextView max_grade_num = (TextView) findViewById(R.id.max_grade_num);
                TextView min_grade_num = (TextView) findViewById(R.id.min_grade_num);
                TextView avg_grade_num = (TextView) findViewById(R.id.avg_grade_num);

                Float max = Collections.max(grades);
                Float min = Collections.min(grades);
                Float avg = (grade_1 + grade_2 + grade_3) / 3;
                max_grade_num.setText(String.valueOf(max));
                min_grade_num.setText(String.valueOf(min));
                avg_grade_num.setText(String.valueOf(avg));

                if (grade_1 >= 90 && grade_1 <= 100){
                    letter_grade_1.setText("A");
                }
                else if (grade_1 >= 80 && grade_1 <= 89){
                    letter_grade_1.setText("B");
                }
                else if (grade_1 >= 70 && grade_1 <= 79){
                    letter_grade_1.setText("C");
                }
                else if (grade_1 >= 60 && grade_1 <= 69){
                    letter_grade_1.setText("D");
                }
                else if (grade_1 <= 60 && grade_1 >= 0){
                    letter_grade_1.setText("F");
                }

                if (grade_2 >= 90 && grade_2 <= 100){
                    letter_grade_2.setText("A");
                }
                else if (grade_2 >= 80 && grade_2 <= 89){
                    letter_grade_2.setText("B");
                }
                else if (grade_2 >= 70 && grade_2 <= 79){
                    letter_grade_2.setText("C");
                }
                else if (grade_2 >= 60 && grade_2 <= 69){
                    letter_grade_2.setText("D");
                }
                else if (grade_2 < 60 && grade_2 >= 0){
                    letter_grade_2.setText("F");
                }

                if (grade_3 >= 90 && grade_3 <= 100){
                    letter_grade_3.setText("A");
                }
                else if (grade_3 >= 80 && grade_3<= 89){
                    letter_grade_3.setText("B");
                }
                else if (grade_3 >= 70 && grade_3 <= 79){
                    letter_grade_3.setText("C");
                }
                else if (grade_3 >= 60 && grade_3 <= 69){
                    letter_grade_3.setText("D");
                }
                else if (grade_3 < 60 && grade_3 >= 0){
                    letter_grade_3.setText("F");
                }

                }
            }
        }
    }
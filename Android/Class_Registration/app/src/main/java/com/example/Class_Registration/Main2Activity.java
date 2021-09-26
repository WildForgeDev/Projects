package com.example.Class_Registration;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import java.util.ArrayList;

public class Main2Activity extends AppCompatActivity {
    Button back;
    ArrayList<String> classes = new ArrayList<>();
    String clear_text = "Please Choose a Class";
    String error_message_2 = "Class already registered for.";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        back = (Button) findViewById(R.id.back_b1);
        back.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                openActivity();
            }
        });
    }

    public void onClickAddClass(View view) {
        Spinner class_choice = (Spinner) findViewById(R.id.class_spinner);
        String choice = String.valueOf(class_choice.getSelectedItem());
        TextView class_1 = (TextView) findViewById(R.id.class_1);
        TextView class_2 = (TextView) findViewById(R.id.class_2);
        TextView class_3 = (TextView) findViewById(R.id.class_3);
        TextView error = (TextView) findViewById(R.id.error_message);

        if(classes.size() == 0) {
            if (choice.equals("CS311T - Mobile Programming")) {
                classes.add("CS311T - Mobile Programming");
            } else if (choice.equals("CS267T - Computer Algorithms")) {
                classes.add("CS267T - Computer Algorithms");
            } else if (choice.equals("CS349T - Software Engineering")) {
                classes.add("CS349T - Software Engineering");
            }
        }

        else if(classes.size() > 0) {
            if (classes.contains(choice)){
                error.setText(error_message_2);
            }
            else if (choice.equals("CS311T - Mobile Programming")) {
                classes.add("CS311T - Mobile Programming");
                error.setText("");

            } else if (choice.equals("CS267T - Computer Algorithms")) {
                classes.add("CS267T - Computer Algorithms");
                error.setText("");

            } else if (choice.equals("CS349T - Software Engineering")) {
                classes.add("CS349T - Software Engineering");
                error.setText("");
            }
        }

        if (classes.size() == 1) {
            class_1.setText(classes.get(0));
        } else if (classes.size() == 2) {
            class_2.setText(classes.get(1));
        } else if (classes.size() == 3) {
            class_3.setText(classes.get(2));
        }
    }

    public void onClickReset(View view) {
        TextView class_1 = (TextView) findViewById(R.id.class_1);
        TextView class_2 = (TextView) findViewById(R.id.class_2);
        TextView class_3 = (TextView) findViewById(R.id.class_3);
        TextView error = (TextView) findViewById(R.id.error_message);
        classes.clear();
        class_1.setText(clear_text);
        class_2.setText(clear_text);
        class_3.setText(clear_text);
        error.setText("");

    }

    public void openActivity(){
        Intent intent = new Intent(Main2Activity.this,
                MainActivity.class);
        intent.putStringArrayListExtra("classes", classes);
        startActivity(intent);
    }
}

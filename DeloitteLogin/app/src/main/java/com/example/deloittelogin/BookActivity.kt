package com.example.deloittelogin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class BookActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_book)
        val home = findViewById<Button>(R.id.homeButton)
        val submit = findViewById<Button>(R.id.submitButton)
        home.setOnClickListener{
            val intent = Intent(this, mainPage::class.java)
            startActivity(intent)
        }
        submit.setOnClickListener{
            val intent = Intent(this, QRActivity::class.java)
            startActivity(intent)
        }

    }
}
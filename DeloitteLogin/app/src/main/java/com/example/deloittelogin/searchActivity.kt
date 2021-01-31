package com.example.deloittelogin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton

class searchActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_search)
        val but = findViewById<ImageButton>(R.id.turtleButton1)
        but.setOnClickListener{
            val intent = Intent(this, ProductActivity::class.java)
            startActivity(intent)
        }
    }
}
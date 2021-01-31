package com.example.deloittelogin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ImageButton

class ProductActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_product)
        val back = findViewById<Button>(R.id.backButton3)
        val reserve = findViewById<Button>(R.id.BookButton3)

        back.setOnClickListener{
            val intent = Intent(this, searchActivity::class.java)
            startActivity(intent)
        }
        reserve.setOnClickListener{
            val intent = Intent(this, BookActivity::class.java)
            startActivity(intent)
        }
    }
}
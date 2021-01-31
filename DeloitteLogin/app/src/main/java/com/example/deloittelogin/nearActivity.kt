package com.example.deloittelogin

import android.content.Intent
import android.media.Image
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.ImageButton

class nearActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_near)

        val back = findViewById<Button>(R.id.backButton2)
        val hm = findViewById<ImageButton>(R.id.imageButtonHM)
        back.setOnClickListener{
            val intent = Intent(this,mainPage::class.java)
            startActivity(intent)
        }
        hm.setOnClickListener{
            val intent = Intent(this,HMActivity::class.java)
            startActivity(intent)
        }


    }
}
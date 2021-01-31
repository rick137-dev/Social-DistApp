package com.example.deloittelogin

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebView
import android.widget.Button
import android.widget.ImageButton

class HMActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_h_m)

        val phone = findViewById<ImageButton>(R.id.phoneButton)
        val product = findViewById<ImageButton>(R.id.productButton)
        val book = findViewById<Button>(R.id.bookButton)
        val myWebView: WebView = findViewById(R.id.webview1)
        myWebView.loadUrl("https://www2.hm.com/it_it/index.html")
        phone.setOnClickListener{
            val u = Uri.parse("tel:" + "3331964592")
            val intent = Intent(Intent.ACTION_DIAL,u)
            startActivity(intent)
        }
        product.setOnClickListener{
            val intent = Intent(this,searchActivity::class.java)
            startActivity(intent)
        }
        book.setOnClickListener{
            val intent = Intent(this,BookActivity::class.java)
            startActivity(intent)
        }
        }


    }

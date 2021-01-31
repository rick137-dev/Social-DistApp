package com.example.deloittelogin
import android.content.Intent
import android.os.Bundle
import android.webkit.WebView
import android.widget.Button
import android.widget.ImageButton
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import com.example.deloittelogin.ui.login.LoginActivity

class mainPage : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main_page)


        val nearyou = findViewById<Button>(R.id.nearyoubutton)
        val reservations = findViewById<Button>(R.id.reservationsbutton)
        val maps = findViewById<ImageButton>(R.id.mapButton)



        nearyou.setOnClickListener{
            val intent = Intent(this,nearActivity::class.java)
            startActivity(intent)
        }
        reservations.setOnClickListener{
            val intent = Intent(this,resActivity::class.java)
            startActivity(intent)
        }
        maps.setOnClickListener{
            val intent = Intent(this,MapsActivity::class.java)
            startActivity(intent)
        }


        }




    }

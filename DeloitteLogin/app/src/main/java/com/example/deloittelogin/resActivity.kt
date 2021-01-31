package com.example.deloittelogin

import android.annotation.SuppressLint
import android.content.Intent
import android.media.Image
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.AlarmClock
import android.provider.AlarmClock.ACTION_SET_ALARM
import android.provider.AlarmClock.ACTION_SET_TIMER
import android.provider.MediaStore
import android.widget.Button
import android.widget.ImageButton

class resActivity : AppCompatActivity() {
    @SuppressLint("WrongViewCast")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_res)

        val back= findViewById<Button>(R.id.backButton)
        val cam = findViewById<ImageButton>(R.id.cameraButton)
        val alarm = findViewById<ImageButton>(R.id.alarmButton)
        back.setOnClickListener{
            val intent = Intent(this,mainPage::class.java)
            startActivity(intent)
        }
        cam.setOnClickListener{
            val cam_intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            startActivity(cam_intent)
        }
        alarm.setOnClickListener{
            val intent = Intent(ACTION_SET_ALARM)
            intent.putExtra(AlarmClock.EXTRA_MINUTES,30)
            intent.putExtra(AlarmClock.EXTRA_HOUR,13)
            intent.putExtra(AlarmClock.EXTRA_MESSAGE,"Sharon Barber")
            startActivity(intent)
        }


    }
}
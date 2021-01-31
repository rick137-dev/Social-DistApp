package com.example.deloittelogin
import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.deloittelogin.ui.login.LoginActivity
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.activity_register.*


class RegisterActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_register)

        val regbutton = findViewById<Button>(R.id.registerButton2)
        val logbutton = findViewById<Button>(R.id.loginButton2)

        val fintent23 = Intent(this, mainPage::class.java)

        logbutton.setOnClickListener{
            val fintent2 = Intent(this, LoginActivity::class.java)
            startActivity(fintent2)


        }





        val username=findViewById<EditText>(R.id.editTextTextPersonName)
        val password = findViewById<EditText>(R.id.editTextTextPassword)
        val email =findViewById<EditText>(R.id.editTextTextEmailAddress)
        val dob =findViewById<EditText>(R.id.editTextPhone)
        val phone =findViewById<EditText>(R.id.editTextPhone2)
        val welcome = "Welcome"


        registerButton2.setOnClickListener(object : View.OnClickListener {
            override fun onClick(view: View?) {
                Toast.makeText(applicationContext,"You are now Registered as Riccardo Caiulo!",Toast.LENGTH_SHORT).show()

                startActivity(fintent23)

            }

        })


    }


}





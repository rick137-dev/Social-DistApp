package com.example.deloittelogin.ui.login

import android.app.Activity
import android.content.Intent
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import android.os.Bundle
import androidx.annotation.StringRes
import androidx.appcompat.app.AppCompatActivity
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.view.inputmethod.EditorInfo
import android.widget.Button
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.Toast

import com.example.deloittelogin.R
import com.example.deloittelogin.RegisterActivity
import com.example.deloittelogin.mainPage
import kotlinx.android.synthetic.main.activity_login.*

class LoginActivity : AppCompatActivity() {

    private lateinit var loginViewModel: LoginViewModel


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)


        setContentView(R.layout.activity_login)
        val registerbutton = findViewById<Button>(R.id.registerButton1)
        val login = findViewById<Button>(R.id.loginButtonA)
        val intent2 = Intent(this, mainPage::class.java)

        registerbutton.setOnClickListener{
            val intent = Intent(this,RegisterActivity::class.java)
            startActivity(intent)
        }



        val username = findViewById<EditText>(R.id.username)
        val password = findViewById<EditText>(R.id.password)

        val loading = findViewById<ProgressBar>(R.id.loading)





            login.setOnClickListener{
                startActivity(intent2)
                Toast.makeText(applicationContext,"Welcome Riccardo Caiulo!",Toast.LENGTH_SHORT).show()
            }
        }
    }






fun EditText.afterTextChanged(afterTextChanged: (String) -> Unit) {
    this.addTextChangedListener(object : TextWatcher {
        override fun afterTextChanged(editable: Editable?) {
            afterTextChanged.invoke(editable.toString())
        }

        override fun beforeTextChanged(s: CharSequence, start: Int, count: Int, after: Int) {}

        override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {}
    })
}
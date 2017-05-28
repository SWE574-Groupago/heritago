package com.heritago.heritandroid.helpers;

/**
 * Created by onurtokoglu on 14/05/2017.
 */

public class LoginHelper {
    public static final LoginHelper shared = new LoginHelper();
    private LoginHelper() {
    }

    public boolean isLoggedIn(){
        return false;
    }

    public String getUsername(){
        return "suzan";
    }
}

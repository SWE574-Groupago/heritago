package com.heritago.heritandroid.model;

/**
 * Created by onurtokoglu on 09/04/2017.
 */

public class HeritageDetail {
    private String key;
    private String value;

    public HeritageDetail() {
    }

    public HeritageDetail(String key, String value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public String getValue() {
        return value;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public void setValue(String value) {
        this.value = value;
    }
}

package com.heritago.heritandroid.model;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class Heritage {
    private String id;
    private String title;
    private String description;
    private String creator;
    public String imageUrl;

    public Heritage(String id, String title, String description, String creator) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.creator = creator;
        this.imageUrl = "http://i.sozcu.com.tr/wp-content/uploads/2015/04/01/670sultanahmetcamii.jpg";
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getCreator() {
        return creator;
    }

    public void setCreator(String creator) {
        this.creator = creator;
    }
}

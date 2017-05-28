package com.heritago.heritandroid.model;

import com.heritago.heritandroid.api.ApiClient;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class Heritage {
    private final String defaultImageUrl = "https://www.proyas.org/wp-content/themes/404/images/placeholder.jpg";
    public String id;
    private String title;
    private String description;
    public String createdAt;
    private List<BasicInformation> basicInformation = new ArrayList<>();
    public List<Origin> origin = new ArrayList<>();
    public List<String> tags = new ArrayList<>();
    public int annotationCount;
    private Owner owner;
    public List<Multimedia> multimedia;


    public Heritage(String id, String title, String description, Owner owner) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.owner = owner;
    }

    public String getThumbnailImageUrl(){
        for (Multimedia m: multimedia){
            if (m.getType().equals(Multimedia.Type.image)){
                return ApiClient.imageBaseUrl + m.url;
            }
        }

        return defaultImageUrl;
    }

    public String getOwnerName(){
        try {
            return owner.name;
        }catch (Exception e){
            return "";
        }
    }

    public String getTitle() {
        return (title != null)? title : "" ;
    }

    public String getDescription() {
        return (title != null)? description : "";
    }

    public List<BasicInformation> getBasicInformation() {
        return (basicInformation != null)? basicInformation : new ArrayList<BasicInformation>();
    }

    public static class Owner {
        public String id;
        public String name;

        public Owner(String id, String name) {
            this.id = id;
            this.name = name;
        }
    }
    public static class Origin {
        public String name;

        public Origin(String name) {
            this.name = name;
        }
    }

    public static class BasicInformation {
        public String name;
        public String value;

        public BasicInformation(String name, String value) {
            this.name = name;
            this.value = value;
        }
    }

    public static class Multimedia {
        public String type;
        public String id;
        private String url;
        public String createdAt;
        public Selector selector;

        public Multimedia(Type t){
            this.type = t.name();
        }

        public Type getType(){
            for (Type t: Type.values()){
                if (this.type.equals(t.name())){
                    return t;
                }
            }
            return Type.unknown;
        }

        public String getUrl(){
            if (url == null) return null;
            return ApiClient.imageBaseUrl + url;
        }

        public class Selector {
            public String type;
            public Object value;
        }
        public enum Type {
            image, video, audio, location, unknown
        }
    }
}

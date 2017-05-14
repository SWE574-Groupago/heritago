package com.heritago.heritandroid.model;

import java.util.List;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class Heritage {
    private final String defaultImageUrl = "http://i.sozcu.com.tr/wp-content/uploads/2015/04/01/670sultanahmetcamii.jpg";
    public String id;
    public String title;
    public String description;
    public String createdAt;
    public List<BasicInformation> basicInformation;
    public List<String> origins;
    public List<String> tags;
    public int annotationCount;
    private Owner owner;
    private List<Multimedia> multimedia;


    public Heritage(String id, String title, String description, Owner owner) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.owner = owner;
    }

    public String getThumbnailImageUrl(){
        for (Multimedia m: multimedia){
            if (m.getType().equals(Multimedia.Type.image)){
                return m.url;
            }
        }

        return defaultImageUrl;
    }

    public String getOwnerName(){
        return owner.name;
    }

    public static class Owner {
        public String id;
        public String name;

        public Owner(String id, String name) {
            this.id = id;
            this.name = name;
        }
    }
    public static class BasicInformation {
        public String key;
        public String value;

        public BasicInformation(String key, String value) {
            this.key = key;
            this.value = value;
        }
    }

    public static class Multimedia {
        public String type;
        public String id;
        public String url;
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

        public class Selector {
            public String type;
            public Object value;
        }
        public enum Type {
            image, video, audio, location, unknown
        }
    }
}

package com.heritago.heritandroid.bus;

import com.heritago.heritandroid.model.Heritage;

/**
 * Created by onurtokoglu on 02/04/2017.
 */

public class DidTapHeritageCardEvent {
    private Heritage heritage;

    public DidTapHeritageCardEvent(Heritage heritage) {
        this.heritage = heritage;
    }

    public Heritage getHeritage() {
        return heritage;
    }
}

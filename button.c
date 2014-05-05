#include <pdextended/m_pd.h>
#include <wiringPi.h>

t_class *button_class;

typedef struct buttonControl
{
    t_object x_obj;
    t_clock *x_clock;
    int defaultButtonState;
    int buttonState;
    int pinNum;
} t_buttonControl;

void buttonlistener_tick(t_buttonControl *x)
{
    int prevState = x->buttonState;
    x->buttonState = digitalRead(x->pinNum);
    if (prevState != x->buttonState)
    {
        if (x->buttonState != x->defaultButtonState) //bang if button has just been pressed
        {
            outlet_bang(x->x_obj.ob_outlet);
        }
    }
    clock_delay(x->x_clock, 1); //polling every millisecond
}

void *buttonlistener_new()
{
    t_buttonControl *x = (t_buttonControl *)pd_new(button_class);
    x->x_clock = clock_new(x, (t_method)buttonlistener_tick);
    outlet_new(&x->x_obj, gensym("bang"));
    //call the tick function once to start it
    x->pinNum = 0; //0 is GPIO 17 in wiringPi
    pinMode(x->pinNum, INPUT);
    x->buttonState = digitalRead(x->pinNum);
    x->defaultButtonState = x->buttonState;
    buttonlistener_tick(x);
    return (x);
}

void buttonlistener_free(t_buttonControl *x)
{
    clock_free(x->x_clock);
}

void buttonlistener_setup()
{
    wiringPiSetupSys();
    button_class = class_new(gensym("buttonlistener"), (t_newmethod)buttonlistener_new,
                                     (t_method)buttonlistener_free, sizeof(t_buttonControl), CLASS_NOINLET, 0);
}
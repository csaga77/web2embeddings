Work in progress

The content of this page was not yet updated for Godot `4.4` and may be
outdated. If you know how to improve this page or you can confirm that it's up
to date, feel free to open a pull request.

# Custom GUI controls

## So many controls...

Yet there are never enough. Creating your own custom controls that act just
the way you want them to is an obsession of almost every GUI programmer. Godot
provides plenty of them, but they may not work exactly the way you want.
Before contacting the developers with a pull-request to support diagonal
scrollbars, at least it will be good to know how to create these controls
easily from script.

## Drawing

For drawing, it is recommended to check the Custom drawing in 2D tutorial. The
same applies. Some functions are worth mentioning due to their usefulness when
drawing, so they will be detailed next:

### Checking control size

Unlike 2D nodes, "size" is important with controls, as it helps to organize
them in proper layouts. For this, the Control.size property is provided.
Checking it during `_draw()` is vital to ensure everything is kept in-bounds.

### Checking focus

Some controls (such as buttons or text editors) might provide input focus for
keyboard or joypad input. Examples of this are entering text or pressing a
button. This is controlled with the Control.focus_mode property. When drawing,
and if the control supports input focus, it is always desired to show some
sort of indicator (highlight, box, etc.) to indicate that this is the
currently focused control. To check for this status, the Control.has_focus()
method exists. Example

GDScriptC#

    
    
    func _draw():
        if has_focus():
             draw_selected()
        else:
             draw_normal()
    
    
    
    public override void _Draw()
    {
        if (HasFocus())
        {
            DrawSelected()
        }
        else
        {
            DrawNormal();
        }
    }
    

## Sizing

As mentioned before, size is important to controls. This allows them to lay
out properly, when set into grids, containers, or anchored. Controls, most of
the time, provide a minimum size to help properly lay them out. For example,
if controls are placed vertically on top of each other using a VBoxContainer,
the minimum size will make sure your custom control is not squished by the
other controls in the container.

To provide this callback, just override Control._get_minimum_size(), for
example:

GDScriptC#

    
    
    func _get_minimum_size():
        return Vector2(30, 30)
    
    
    
    public override Vector2 _GetMinimumSize()
    {
        return new Vector2(20, 20);
    }
    

Alternatively, set it using a function:

GDScriptC#

    
    
    func _ready():
        set_custom_minimum_size(Vector2(30, 30))
    
    
    
    public override void _Ready()
    {
        CustomMinimumSize = new Vector2(20, 20);
    }
    

## Input

Controls provide a few helpers to make managing input events much easier than
regular nodes.

### Input events

There are a few tutorials about input before this one, but it's worth
mentioning that controls have a special input method that only works when:

  * The mouse pointer is over the control.

  * The button was pressed over this control (control always captures input until button is released)

  * Control provides keyboard/joypad focus via Control.focus_mode.

This function is Control._gui_input(). To use it, override it in your control.
No processing needs to be set.

GDScriptC#

    
    
    extends Control
    
    func _gui_input(event):
       if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
           print("Left mouse button was pressed!")
    
    
    
    public override void _GuiInput(InputEvent @event)
    {
        if (@event is InputEventMouseButton mbe && mbe.ButtonIndex == MouseButton.Left && mbe.Pressed)
        {
            GD.Print("Left mouse button was pressed!");
        }
    }
    

For more information about events themselves, check the Using InputEvent
tutorial.

### Notifications

Controls also have many useful notifications for which no dedicated callback
exists, but which can be checked with the _notification callback:

GDScriptC#

    
    
    func _notification(what):
        match what:
            NOTIFICATION_MOUSE_ENTER:
                pass # Mouse entered the area of this control.
            NOTIFICATION_MOUSE_EXIT:
                pass # Mouse exited the area of this control.
            NOTIFICATION_FOCUS_ENTER:
                pass # Control gained focus.
            NOTIFICATION_FOCUS_EXIT:
                pass # Control lost focus.
            NOTIFICATION_THEME_CHANGED:
                pass # Theme used to draw the control changed;
                # update and redraw is recommended if using a theme.
            NOTIFICATION_VISIBILITY_CHANGED:
                pass # Control became visible/invisible;
                # check new status with is_visible().
            NOTIFICATION_RESIZED:
                pass # Control changed size; check new size
                # with get_size().
            NOTIFICATION_MODAL_CLOSE:
                pass # For modal pop-ups, notification
                # that the pop-up was closed.
    
    
    
    public override void _Notification(int what)
    {
        switch (what)
        {
            case NotificationMouseEnter:
                // Mouse entered the area of this control.
                break;
    
            case NotificationMouseExit:
                // Mouse exited the area of this control.
                break;
    
            case NotificationFocusEnter:
                // Control gained focus.
                break;
    
            case NotificationFocusExit:
                // Control lost focus.
                break;
    
            case NotificationThemeChanged:
                // Theme used to draw the control changed;
                // update and redraw is recommended if using a theme.
                break;
    
            case NotificationVisibilityChanged:
                // Control became visible/invisible;
                // check new status with is_visible().
                break;
    
            case NotificationResized:
                // Control changed size; check new size with get_size().
                break;
    
            case NotificationModalClose:
                // For modal pop-ups, notification that the pop-up was closed.
                break;
        }
    }
    

## User-contributed notes

Please read the User-contributed notes policy before submitting a comment.

* * *

Built with Sphinx using a theme provided by Read the Docs.


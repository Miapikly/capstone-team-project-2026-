ini python:
    def dragged_func(dragged_items, dropped_on):
        if dropped_on is not None:
            if dragged_items[0].drag_raise == True:
                dragged_items[0].snap(dropped_on.x, dropped_on.y)

screen drag_drop:
    image Solid("#ffffff")
    draggroup:
        drag:
            align (0.3, 0.5)
            drag_raise True
            drag_name "pink"
            dragged dragged_func
            image Solid("#ff9b94") xysize(250, 250)
        drag:
            align (0.5, 0.5)
            drag_raise True
            drag_name "yellow"
            dragged dragged_func
            image Solid("#ffd53d") xysize(250, 250)
        drag:
            align (0.7, 0.5)
            drag_raise True
            drag_name "green"
            dragged dragged_func
            image Solid("#9fde6f") xysize(250, 250)

    add my_draggroup

default pink_drag = Drag(d = Solid("#ff9b94", xysize = (250, 250)), drag_name = "pink", drag_raise = true, align = (0.3, 0.5))
default yellow_drag = Drag(d = Solid("#ffd53d", xysize = (250, 250)), drag_name = "yellow", drag_raise = true, align = (0.5, 0.5))
default green_drag = Drag(d = Solid("#9fde6f", xysize = (250, 250)), drag_name = "green", drag_raise = true, align = (0.8, 0.5))
default my_draggroup = DragGroup(pink_drag, yellow_drag, green_drag)

define config.longpress_duration = 0.5

label start:
    call screen drag_drop
    return

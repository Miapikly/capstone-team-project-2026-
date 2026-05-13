screen drag_drop:
    image Solid("#ffffff")
    draggroup:
        drag:
            align (0.3, 0.5)
            drag_raise True
            drag_name "pink"
            drag_handle (0.5, 0.5, 100, 100)
            image Solid("#ff9b94") xysize(250, 250)
        drag:
            align (0.5, 0.5)
            drag_raise True
            drag_name "yellow"
            drag_handle (0.5, 0.5, 100, 100)
            image Solid("#ffd53d") xysize(250, 250)
        drag:
            align (0.7, 0.5)
            drag_raise True
            drag_name "green"
            drag_handle (0.5, 0.5, 100, 100)
            image Solid("#9fde6f") xysize(250, 250)

label start:
    call screen drag_drop
    return
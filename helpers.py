from turtle import tracer,delay,update,forward,backward,penup,pendown,write,position,heading,goto,setheading,left,right,pencolor,clearscreen,speed,hideturtle

class no_delay:
    "A context manager which causes drawing code to run instantly"

    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)

plot_settings = {}

def clamp_point(x, domain):
    if x < domain[0]:
        return domain[0]
    if x > domain[1]:
        return domain[1]
    return x

def clamp_database(db, x_domain, y_domain):
    for i in range(len(db)):
        x_clamp = clamp_point(db.iloc[i][0], x_domain)
        y_clamp = clamp_point(db.iloc[i][1], y_domain)
        db.iloc[i, 0] = x_clamp
        db.iloc[i, 1] = y_clamp
    return db

def scale(x, old_domain, new_domain):
    old_ldiff = x - old_domain[0]
    total_old_diff = old_domain[1] - old_domain[0]
    old_percent_pos = old_ldiff/total_old_diff
    total_new_diff = new_domain[1] - new_domain[0]
    new_ldiff = old_percent_pos * total_new_diff
    new_x = new_ldiff + new_domain[0]
    return new_x

def draw_tick():
    pendown()
    forward(plot_settings['tick_size']/2)
    backward(plot_settings['tick_size'])
    forward(plot_settings['tick_size']/2)
    penup()

def label_tick(num):
    forward(plot_settings['tick_size']*5)
    write("{}".format(num), move=False, align="center", font=("Arial", 8, "normal"))
    backward(plot_settings['tick_size']*5)

def draw_x_axis():
    start_pos = position()
    start_head = heading()
    penup()
    goto(plot_settings['turtle_x_axis_domain'][0], plot_settings['turtle_y_axis_domain'][0])
    setheading(0)
    pendown()

    start = plot_settings['data_x_axis_domain'][0]
    end = plot_settings['data_x_axis_domain'][1]
    length = plot_settings['turtle_x_axis_domain'][1] - plot_settings['turtle_x_axis_domain'][0]
    increment = plot_settings['x_axis_increment']
    num_increments = (end-start)/increment
    scaled_increment = (length-0)/num_increments
    for i in range(start, end, increment):
        right(90)
        draw_tick()
        label_tick(i)
        left(90)
        pendown()
        forward(scaled_increment)
    right(90)
    draw_tick()
    label_tick(plot_settings['data_x_axis_domain'][1])

    # labelling axis
    penup()
    label_x_pos = (plot_settings['turtle_x_axis_domain'][1]-plot_settings['turtle_x_axis_domain'][0])/2 + plot_settings['turtle_x_axis_domain'][0]
    label_y_pos = plot_settings['turtle_y_axis_domain'][0]
    goto(label_x_pos, label_y_pos)
    forward(plot_settings['tick_size']*10)
    write("{}".format(plot_settings['x_label']), move=False, align="center", font=("Arial", 8, "normal"))

    penup()
    goto(start_pos)
    setheading(start_head)

def draw_y_axis():
    start_pos = position()
    start_head = heading()
    penup()
    goto(plot_settings['turtle_x_axis_domain'][0], plot_settings['turtle_y_axis_domain'][0])
    setheading(90)
    pendown()

    start = plot_settings['data_y_axis_domain'][0]
    end = plot_settings['data_y_axis_domain'][1]
    length = plot_settings['turtle_y_axis_domain'][1] - plot_settings['turtle_y_axis_domain'][0]
    increment = plot_settings['y_axis_increment']
    num_increments = (end-start)/increment
    scaled_increment = (length-0)/num_increments
    for i in range(start, end, increment):
        left(90)
        draw_tick()
        label_tick(i)
        right(90)
        pendown()
        forward(scaled_increment)
    left(90)
    draw_tick()
    label_tick(plot_settings['data_y_axis_domain'][1])

    # labelling axis
    penup()
    label_x_pos = plot_settings['turtle_x_axis_domain'][0]
    label_y_pos = (plot_settings['turtle_y_axis_domain'][1]-plot_settings['turtle_y_axis_domain'][0])/2 + plot_settings['turtle_y_axis_domain'][0]
    goto(label_x_pos, label_y_pos)
    forward(plot_settings['tick_size']*10)
    write("{}".format(plot_settings['y_label']), move=False, align="center", font=("Arial", 8, "normal"))

    penup()
    goto(start_pos)
    setheading(start_head)

def draw_bounding_box():
    start_pos = position()
    start_head = heading()
    penup()
    goto(plot_settings['turtle_x_axis_domain'][0], plot_settings['turtle_y_axis_domain'][1])
    pendown()
    goto(plot_settings['turtle_x_axis_domain'][1], plot_settings['turtle_y_axis_domain'][1])
    goto(plot_settings['turtle_x_axis_domain'][1], plot_settings['turtle_y_axis_domain'][0])
    penup()
    goto(start_pos)
    setheading(start_head)

def make_cross():
    pendown()
    pencolor('blue')
    setheading(0)
    for i in range(2):
        forward(plot_settings['tick_size']/2)
        backward(plot_settings['tick_size'])
        forward(plot_settings['tick_size']/2)
        right(90)
    penup()

def plot_points(data_points_list):
    plot_x_domain = (plot_settings['data_x_axis_domain'][0], plot_settings['data_x_axis_domain'][1])
    plot_y_domain = (plot_settings['data_y_axis_domain'][0], plot_settings['data_y_axis_domain'][1])

    turtle_x_domain = (plot_settings['turtle_x_axis_domain'][0], plot_settings['turtle_x_axis_domain'][1])
    turtle_y_domain = (plot_settings['turtle_x_axis_domain'][0], plot_settings['turtle_x_axis_domain'][1])

    start_pos = position()
    start_head = heading()
    for x,y in data_points_list:
        x_scaled = scale(x, plot_x_domain, turtle_x_domain)
        y_scaled = scale(y, plot_y_domain, turtle_y_domain)
        penup()
        goto(x_scaled, y_scaled)
        make_cross()

    penup()
    goto(start_pos)
    setheading(start_head)

def draw_scatter_plot(data_points_list, x_label, y_label, turtle_x_axis_domain = (-150,150), turtle_y_axis_domain = (-150,150), data_x_axis_domain = None, x_axis_increment = 10, data_y_axis_domain = None, y_axis_increment = 10, tick_size = 4):
    plot_settings['x_label'] = x_label
    plot_settings['y_label'] = y_label
    plot_settings['turtle_x_axis_domain'] = turtle_x_axis_domain
    plot_settings['turtle_y_axis_domain'] = turtle_y_axis_domain
    plot_settings['data_x_axis_domain'] = data_x_axis_domain if data_x_axis_domain else (int(min(point[0] for point in data_points_list) - x_axis_increment), int(max(point[0] for point in data_points_list) + x_axis_increment))
    plot_settings['x_axis_increment'] = x_axis_increment
    plot_settings['data_y_axis_domain'] = data_y_axis_domain if data_x_axis_domain else (int(min(point[1] for point in data_points_list) - y_axis_increment), int(max(point[1] for point in data_points_list) + y_axis_increment))
    plot_settings['y_axis_increment'] = y_axis_increment
    plot_settings['tick_size'] = tick_size
    clearscreen()
    with no_delay():
        draw_x_axis()
        draw_y_axis()
        draw_bounding_box()
        plot_points(data_points_list)
        hideturtle()
    return plot_settings

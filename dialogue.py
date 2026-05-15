class DialogBox:
    def __init__(self, x, y, w, h, text):
    	# .... Initialize data

        self.lines = []
        self.char_count = 0 # Number of characters in self.lines.
        self.paint_count = 0 # Number of characters to paint in self.render
        self.set_text(text)

    def set_text(self, text):
        self.lines = text.split('\n')
        self.char_count = sum(len(line) for line in self.lines)
        self.paint_count = 0 # Start adding letters from the start.

    def render(self):
        # .... Get surface to paint.

        # Draw one more character if possible.
        self.paint_count = min(self.paint_count + 1, self.char_count)

        # Draw the text.
        y = 25
        chars_to_draw = self.paint_count
        for line in self.lines:
            if len(line) < chars_to_draw:
                line = line[:chars_to_draw]

            # .... paint 'line' at (25, y)
            y += 50

            chars_to_draw = chars_to_draw - len(line)
            if chars_to_draw <= 0:
                break

        # .... Display painted text
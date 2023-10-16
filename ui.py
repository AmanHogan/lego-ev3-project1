

class NavController:

    def __init__(self, origin_frame):
        self.origin_frame = origin_frame
        self.current_frame = origin_frame

    def get_frame(self):
        return self.current_frame

    def update_frame(self):
        pass

    def print_frame(self):
        pass

# Example usage
if __name__ == "__main__":
    NavController([0, 1, 0])
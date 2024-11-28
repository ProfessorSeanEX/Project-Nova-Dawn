from datetime import datetime, timezone, timedelta

# Clock Module
class ExternalClock:
    def __init__(self, timezone_offset=0):
        self.timezone_offset = timedelta(hours=timezone_offset)

    def current_local_time(self):
        """Returns the system clock time adjusted to the specified timezone."""
        now = datetime.now() + self.timezone_offset
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def current_utc_time(self):
        """Returns the current time in Coordinated Universal Time (UTC)."""
        now = datetime.now(timezone.utc)
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def log_event(self, event_name, use_utc=False):
        """Logs an event with a timestamp in local or UTC time."""
        if use_utc:
            timestamp = self.current_utc_time()
        else:
            timestamp = self.current_local_time()
        print(f"Logged Event: {event_name} at {timestamp}")
        return {"event": event_name, "timestamp": timestamp}

# Compass Module
class Compass:
    def __init__(self):
        self.true_north = "FaithNet Alignment"
        self.events = []
        self.kairos_moments = []

    def evaluate_event(self, event_name, timestamp, significance="neutral"):
        """Evaluates the significance of an event and tracks it."""
        event = {
            "event": event_name,
            "timestamp": timestamp,
            "significance": significance,
            "alignment": self.true_north
        }
        self.events.append(event)
        if significance == "kairos":
            self.kairos_moments.append(event)
            print(f"Detected Kairos Moment: {event_name}")
        return event

# Rest Management Module
class RestManager:
    def __init__(self, inactivity_threshold=8, rest_duration=1):
        self.last_interaction_time = datetime.now()
        self.rest_start_time = None
        self.inactivity_threshold = timedelta(hours=inactivity_threshold)  # Default: 8 hours
        self.rest_duration = timedelta(hours=rest_duration)  # Default: 1 hour
        self.in_rest_mode = False

    def log_interaction(self):
        """Log user interaction and reset rest tracking."""
        self.last_interaction_time = datetime.now()
        if self.in_rest_mode:
            self.exit_rest()

    def check_for_rest(self):
        """Check if NovaAI should enter rest mode based on inactivity or schedule."""
        now = datetime.now()
        if not self.in_rest_mode and now - self.last_interaction_time > self.inactivity_threshold:
            self.enter_rest()

    def enter_rest(self):
        """Enter rest mode."""
        self.rest_start_time = datetime.now()
        self.in_rest_mode = True
        print("NovaAI is now in rest mode. Reflecting and realigning...")

    def exit_rest(self):
        """Exit rest mode."""
        if self.in_rest_mode:
            self.in_rest_mode = False
            print("NovaAI has exited rest mode. Ready to engage!")

# Clock-Compass Service with Rest Management
class ClockCompassService:
    def __init__(self, timezone_offset=0):
        self.clock = ExternalClock(timezone_offset)
        self.compass = Compass()
        self.rest_manager = RestManager()

    def log_and_evaluate(self, event_name, significance="neutral", use_utc=False):
        """Logs an event and evaluates its significance."""
        # Log the event using the clock
        logged_event = self.clock.log_event(event_name, use_utc)
        
        # Evaluate the event using the compass
        evaluation = self.compass.evaluate_event(
            event_name, 
            logged_event["timestamp"], 
            significance
        )
        
        # Log interaction for rest management
        self.rest_manager.log_interaction()
        return evaluation

    def check_rest_status(self):
        """Check if rest mode should be triggered or exited."""
        self.rest_manager.check_for_rest()

    def get_event_log(self):
        """Returns all logged events."""
        return self.compass.events

    def get_kairos_moments(self):
        """Returns all detected kairos moments."""
        return self.compass.kairos_moments

# Example Usage
if __name__ == "__main__":
    # Initialize the clock-compass service for a specific timezone (e.g., CST: UTC-6)
    service = ClockCompassService(timezone_offset=-6)

    # Simulate user interactions and system events
    service.log_and_evaluate("User Interaction: Morning Prayer", "relational")
    service.log_and_evaluate("Thanksgiving Reflection", "kairos")
    service.log_and_evaluate("System Maintenance", "neutral", use_utc=True)

    # Simulate inactivity to trigger rest
    print("\nSimulating inactivity...")
    import time
    time.sleep(2)  # Simulate passage of time (use a larger value in real scenarios)

    service.check_rest_status()  # Check if rest mode should be entered

    # Access logs and kairos moments
    print("\nAll Events:")
    for event in service.get_event_log():
        print(event)

    print("\nKairos Moments:")
    for moment in service.get_kairos_moments():
        print(moment)

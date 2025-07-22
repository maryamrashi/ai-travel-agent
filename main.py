
from agents.destination_agent import suggest_destination
from agents.booking_agent import book_trip
from agents.explore_agent import explore_destination

print("🧳 Welcome to the AI Travel Designer Agent!")
print("Type 'plan:' followed by your mood or interest to get a destination.")
print("Type 'book:' followed by a destination to simulate booking.")
print("Type 'explore:' followed by a destination to explore activities.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("👩‍💼 You: ")

    if user_input.lower() == "exit":
        print("👋 Safe travels! Goodbye!")
        break

    try:
        if user_input.startswith("plan:"):
            mood = user_input[len("plan:"):].strip()
            destination = suggest_destination(mood)
            print(f"\n🗺️ Suggested Destination: {destination}\n")

        elif user_input.startswith("book:"):
            destination = user_input[len("book:"):].strip()
            booking = book_trip(destination)
            print(f"\n📦 Booking Details:\n{booking}\n")

        elif user_input.startswith("explore:"):
            destination = user_input[len("explore:"):].strip()
            places = explore_destination(destination)
            print(f"\n🍽️ Explore Plan:\n{places}\n")

        else:
            print("⚠️ Unknown command. Try 'plan:', 'book:', or 'explore:'.")

    except Exception as e:
        print("❌ Error:", e)
        print("Please try again.")

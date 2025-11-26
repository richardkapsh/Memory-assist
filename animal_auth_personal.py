import requests
import json
import os

class AnimalAuthenticator:
    def __init__(self):
        #Fetch the key from the environment variable
        self.api_key = os.getenv('ANIMAL_API_KEY')
        if not self.api_key:
            raise ValueError("❌ ERROR: The 'ANIMAL_API_KEY' environment variable is not set.")
        self.api_url = "https://api.api-ninjas.com/v1/animals"        
        
        #MANUAL OVERRIDE for problematic animals
        self.known_animals = {
            "dog": "canis lupus familiaris",
            "domestic dog": "canis lupus familiaris", 
            "cat": "felis catus",
            "domestic cat": "felis catus",
            "african wild dog": "lycaon pictus"
        }
    
    def get_animal_facts(self, animal_name):
        """Fetch animal facts from the API with better query handling"""
        try:
            #Construct the request URL with the animal name
            api_endpoint = f"{self.api_url}?name={animal_name}"
            
            #Example: Using a 'fields' parameter to request only specific data (if the API supports it)
            #api_endpoint += "&fields=name,taxonomy,characteristics" 
            
            headers = {'X-Api-Key': self.api_key}
            response = requests.get(api_endpoint, headers=headers)
            
            #Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                return data[0] if data else None
            else:
                #Provide more specific error information
                print(f"❌ API Error {response.status_code}: {response.text}") 
                return None
                    
        except Exception as e:
            print(f"❌ Error fetching animal data: {e}")
            return None    
    
    def create_challenge(self, animal_data, animal_name):
        """Create authentication challenge"""
        if animal_data.get('taxonomy') and animal_data['taxonomy'].get('scientific_name'):
            return {
                'question': f"What is the scientific name of {animal_name}?",
                'answer': animal_data['taxonomy']['scientific_name'].lower()
            }
        return None
    
    def authenticate_animal(self):
        """Main authentication flow"""
        print("🐾 Welcome to Animal Authentication Password System! 🐾")
        print("=" * 50)
        
        while True:
            animal_name = input("\nEnter your favorite animal name (or 'quit' to exit): ").strip()
            
            if animal_name.lower() == 'quit':
                print("👋 Goodbye!")
                break
            
            if not animal_name:
                print("❌ Please enter your favorite animal name!")
                continue
            
            print(f"🔍 Searching for {animal_name} facts...")
            
            animal_data = self.get_animal_facts(animal_name)
            
            if not animal_data:
                print(f"❌ No data found for '{animal_name}'. Try: tiger, elephant, eagle, etc.")
                continue
            
            challenge = self.create_challenge(animal_data, animal_name)
            
            if not challenge:
                print("❌ Not enough data for authentication challenge.")
                continue
            
            print(f"🔐 {challenge['question']}")
            user_answer = input("Your answer: ").strip().lower()
            
            if user_answer == challenge['answer']:
                print(f"🎉 Authentication successful! Welcome, {animal_name}!")
                print("🌟 You now have successfully typed in your password!")
            else:
                print(f"❌ Password is unsuccessful!")
                print(f"💡 The answer was: {challenge['answer'].title()}")

#Run it if this file is run directly
if __name__ == "__main__":
    auth_system = AnimalAuthenticator()
    auth_system.authenticate_animal()


from collections import Counter

class BasicTokenizer:
    
    def train(self, text, vocab_size, verbose=False):
        current_vocab_size = 256
        # Inititalize vocabulary
        vocab =  {chr(i): i for i in range(256)}
        
        # Convert to UTF-8
        text_bytes = [element for element in bytearray( text.encode('utf-8'))]
        print(text)
        print(text_bytes)
        # Iterate on the element and count pairs of tokens.
        while len(vocab) <= vocab_size:
            print(f'{len(vocab)=}')
            
            # Encode 
            text_encoded = []
            text_location = 0
            while text_location < len(text):
                for substring,token in vocab.items():
                    if text[text_location:].startswith(substring):
                        text_encoded.append(token)
                        text_location += len(substring)
                        break
            # Calculate most common token
            counts = Counter([(a,b) for a,b in zip(text_encoded, text_encoded[1:])])
            
            # Take the most frequent tokens
            most_common_pair, pair_count = counts.most_common(1)[0]
            most_common_pair = chr(most_common_pair[0]) +  chr(most_common_pair[1])
            print(f'{most_common_pair=}')
            
            # Assign a new token 
            vocab = {**{most_common_pair: len(vocab)+1}, **vocab}
            
            # Encode again
            a=1 
    def encode(self, text):
        pass
    def decode(self, ids):
        pass
    
    
    
if __name__ == "__main__":
    # Load text file
    with open("tests/taylorswift.txt", "r") as f:
        text = f.read()
    text = text[:100]
    vocab_size = 500
    # Train
    
    tokenizer = BasicTokenizer()
    tokenizer.train(text, vocab_size, verbose=False)
    # ids = tokenizer.encode(text)
    # text = tokenizer.decode(ids)
# dataset.py
import torch
from torch.utils.data import Dataset

class CommonsenseQADataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length=128):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        
        # Map answer keys to indices
        self.label_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        example = self.dataset[idx]
        question = example["question"]
        choices = example["choices"]["text"]
        label = self.label_map[example["answerKey"]]
        
        # Format as per RobertaForMultipleChoice requirements
        encoding = self.tokenizer(
            [[question, choice] for choice in choices],
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )
        
        # Reshape the input tensors
        input_ids = encoding.input_ids.view(-1, 5, self.max_length)
        attention_mask = encoding.attention_mask.view(-1, 5, self.max_length)
        
        return {
            "input_ids": input_ids.squeeze(0),
            "attention_mask": attention_mask.squeeze(0),
            "labels": torch.tensor(label)
        }
        
        
        
class OptimizedCommonsenseQADataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length=128, cache_tokenization=True):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.cache_tokenization = cache_tokenization
        
        # Map answer keys to indices
        self.label_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        
        # Pre-process and cache tokenized inputs if enabled
        self.cached_features = None
        if self.cache_tokenization:
            self.cached_features = self._create_features()
    
    def _create_features(self):
        """Pre-tokenize all examples and cache them"""
        features = []
        for i in range(len(self.dataset)):
            example = self.dataset[i]
            question = example["question"]
            choices = example["choices"]["text"]
            label = self.label_map[example["answerKey"]]
            
            encoding = self.tokenizer(
                [[question, choice] for choice in choices],
                padding="max_length",
                truncation=True,
                max_length=self.max_length,
                return_tensors="pt"
            )
            
            # Create a single batch for each example
            features.append({
                "input_ids": encoding.input_ids.view(-1, 5, self.max_length).squeeze(0),
                "attention_mask": encoding.attention_mask.view(-1, 5, self.max_length).squeeze(0),
                "labels": torch.tensor(label)
            })
        return features
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        if self.cached_features is not None:
            return self.cached_features[idx]
        
        # Fall back to on-the-fly processing if caching is disabled
        example = self.dataset[idx]
        question = example["question"]
        choices = example["choices"]["text"]
        label = self.label_map[example["answerKey"]]
        
        encoding = self.tokenizer(
            [[question, choice] for choice in choices],
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )
        
        return {
            "input_ids": encoding.input_ids.view(-1, 5, self.max_length).squeeze(0),
            "attention_mask": encoding.attention_mask.view(-1, 5, self.max_length).squeeze(0),
            "labels": torch.tensor(label)
        }
class HashTable:
    def __init__(self, initial_size=8, load_factor=0.75):
        self.size = initial_size
        self.count = 0
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def _resize(self, new_size):
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def _should_resize(self):
        return self.count / self.size > self.load_factor

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self._should_resize():
            self._resize(self.size * 2)

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        return default

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.count -= 1

                if self.size > 8 and self.count / self.size < 0.25:
                    self._resize(max(8, self.size // 2))

                return True

        return False

    def contains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return True
        return False

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        value = self.get(key)
        if value is None and not self.contains(key):
            raise KeyError(f"Key '{key}' not found")
        return value

    def __delitem__(self, key):
        if not self.delete(key):
            raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        return self.contains(key)

    def __len__(self):
        return self.count

    def keys(self):
        keys_list = []
        for bucket in self.buckets:
            for key, value in bucket:
                keys_list.append(key)
        return keys_list

    def values(self):
        values_list = []
        for bucket in self.buckets:
            for key, value in bucket:
                values_list.append(value)
        return values_list

    def items(self):
        items_list = []
        for bucket in self.buckets:
            for item in bucket:
                items_list.append(item)
        return items_list

    def __str__(self):
        items = []
        for bucket in self.buckets:
            for key, value in bucket:
                items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"
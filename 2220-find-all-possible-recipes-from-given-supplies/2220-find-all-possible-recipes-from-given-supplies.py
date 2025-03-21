class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)
        
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
        
        available = set(supplies)
        queue = deque(supplies)
        result = []
        
        while queue:
            ingredient = queue.popleft()
            for recipe in graph[ingredient]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        
        return result
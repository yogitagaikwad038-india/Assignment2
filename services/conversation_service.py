class ConversationService:

    def execute(
            self,
            chain,
            query
    ):

        return chain.invoke(
            {
                "query": query
            }
        )
dic_article = {
    1: 'article/Diabetes Overview.html',
    2: 'article/Blood glucose management.html'
}

forum_data = [
    {
        "id": 1,
        "title": "high blood sugar",
        "Q": "Is high blood sugar the same as diabetes? What is the first signs of being a diabetic?",
        "A": [
            "High blood sugar does not necessarily mean diabetes. High blood sugar can occur in some physiological circumstances, such as emotional excitement leads to the excitation of the sympathetic nervous system, prompting the secretion of adrenaline and so on to increase the blood sugar concentration. One-time intake of a large amount of sugar, blood sugar can also rise sharply. However, diabetes is a chronic metabolic disease characterized by persistent high blood sugar, only persistent high blood sugar in multiple tests can be diagnosed as diabetes.",
            "Early diabetes may not have obvious subjective symptoms or worrisome clinical manifestations. However, I will advise you to consult a doctor for further examination if you experience symptoms like frequent feelings of thirst, with a marked increase in fluid intake; abnormal increase in appetite; a significant increase in urination frequency and rapid weight decline without intentionally losing weight."
        ]
    },
    {
        "id": 2,
        "title": "drink for people with type 2 diabetes",
        "Q": "What drinks should people with type 2 diabetes avoid and what drinks are best for type 2 diabetes?",
        "A": [
            "Sugar is a big no-no for folks with diabetes when it comes to drinks. Those sugary beverages can send your blood sugar levels soaring and pack a ton of extra calories without much nutrition. I think water is the best one to choose. Managing type 2 diabetes is super important, and watching your sugar intake—whether in drinks or food—is key. By making smart choices, you can keep your blood sugar in check and reduce your risk of complications.",
            "Alcoholic drinks: Drinking alcohol in moderation can be okay, but it can mess with your blood sugar levels and add a bunch of calories. The American Diabetes Association (ADA) says it's best to stick to one drink a day for women and two for men.\n" +
            "Sports drinks and energy drinks: These are basically like fruit juice, but with even more sugar and zero nutritional value. They can really mess with your blood sugar control and make you gain weight.\n" +
            "Sweetened and unsweetened fruit juices: While fruits are good for you, they're also naturally high in sugar. Drinking fruit juice can spike your blood sugar levels, so it's better to eat whole fruits instead. They've got more fiber, which helps keep your blood sugar more stable.\n" +
            "Sodas: Regularly drinking soda can up your chances of getting type 2 diabetes by 26%. They're loaded with added sugar and calories, so it's best to avoid them if you have diabetes.\n" +
            "Sweet tea: This one's tricky because the amount of sugar in sweet tea can vary a lot. It's best to go for unsweetened tea to be safe.\n" +
            "Of course water. Health experts say we should aim for about 4-6 cups of water a day to stay healthy. Water is the best choice for staying hydrated, especially if you have type 2 diabetes, because it has no sugar, carbs, or anything else that can turn into glucose in your body.",
            "Drinking enough water helps your body get rid of extra glucose through urine. For us with type 2 diabetes, drinking plenty of water each day can really help keep our blood sugar levels in check and manage the disease.\nIf plain water feels a bit boring, you can add a little flavor without sacrificing the health benefits. Try adding fresh herbs like mint, basil, or lemon balm, berries like raspberries, slices of lemon, lime, or orange, or cucumber slices.",
            "Herbal teas might be helpful. Herbs have been used for ages to manage diabetes and other chronic illnesses. Herbal teas are a great option because they're low in carbs, calories, and sugar, but high in antioxidants, which can help fight diseases. Some herbs and teas can help manage diabetes by lowering blood sugar levels, increasing insulin action, improving insulin sensitivity, and reducing lipid levels. Some good ones to try include green tea, pomegranate, onion, garlic, ginger, turmeric, cinnamon, cayenne, and American ginseng. For the best results, drink herbal teas without adding extra flavors or sugar. This helps protect the healing compounds in the herbs and prevents any unwanted side effects."
        ]
    },
    {
        "id": 3,
        "title": "what should I do",
        "Q": "My partner has been diagnosed with diabetes, what should I do?",
        "A": [
            "First you should learn to understand diabetes. Get to know the following things: The significance of blood sugar and how it affects health, factors that influence blood sugar levels, daily habits to maintain healthy blood sugar levels, symptoms of high and low blood sugar, when emergency care might be necessary, potential complications and prevention strategies. The more you comprehend about diabetes management, the more empathetic you can be toward your loved one's experiences. You can also attend medical appointments with them, taking notes and asking questions to better understand their doctor's guidance. Consider joining classes offered by their care team to learn about lifestyle changes, such as healthier eating and regular exercise. Discuss what you've learned together and brainstorm ways to implement these changes collectively.",
            "You need to be empathetic and try to offer support and encouragement. Living with diabetes is a constant challenge. Instead of focusing on their missteps, acknowledge their efforts and achievements. You can say like this 'I'm proud of you for checking your blood sugar every morning this week. It's not easy, but you're making great progress!'"
        ]
    }
]

if __name__ == '__main__':
    # 将问题和回答整理成字典
    qa_dict = {}
    for item in forum_data:
        qa_dict[item["Q"]] = item["A"]

    # 打印字典
    for question, answers in qa_dict.items():
        print("Q:", question)
        for index, answer in enumerate(answers):
            print("A{}:".format(index + 1), answer)
        print()

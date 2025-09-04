import json

# Vocabulary lists: topic -> list of (word, translation)
vocab_data = {
    'Family': [
        ('father', 'cha'), ('mother', 'mẹ'), ('brother', 'anh trai'), ('sister', 'chị gái'), ('grandfather', 'ông'),
        ('grandmother', 'bà'), ('son', 'con trai'), ('daughter', 'con gái'), ('uncle', 'chú/ bác'), ('aunt', 'cô/ dì'),
        ('cousin', 'anh chị em họ'), ('nephew', 'cháu trai'), ('niece', 'cháu gái'), ('husband', 'chồng'), ('wife', 'vợ'),
        ('parents', 'bố mẹ'), ('child', 'đứa trẻ'), ('relative', 'họ hàng'), ('family', 'gia đình'), ('baby', 'em bé'),
        ('teenager', 'thiếu niên'), ('adult', 'người lớn'), ('spouse', 'vợ/chồng'), ('twins', 'cặp song sinh'), ('generation', 'thế hệ')
    ],
    'Food': [
        ('rice', 'cơm'), ('bread', 'bánh mì'), ('chicken', 'thịt gà'), ('fish', 'cá'), ('vegetable', 'rau'),
        ('fruit', 'trái cây'), ('soup', 'súp'), ('milk', 'sữa'), ('meat', 'thịt'), ('water', 'nước'),
        ('salad', 'rau trộn'), ('juice', 'nước ép'), ('egg', 'trứng'), ('noodle', 'mì'), ('sugar', 'đường'),
        ('salt', 'muối'), ('pepper', 'tiêu'), ('oil', 'dầu'), ('cheese', 'pho mát'), ('coffee', 'cà phê'),
        ('tea', 'trà'), ('cake', 'bánh'), ('butter', 'bơ'), ('potato', 'khoai tây'), ('tomato', 'cà chua')
    ],
    'Travel': [
        ('plane', 'máy bay'), ('train', 'tàu hỏa'), ('bus', 'xe buýt'), ('car', 'xe hơi'), ('ticket', 'vé'),
        ('passport', 'hộ chiếu'), ('luggage', 'hành lý'), ('hotel', 'khách sạn'), ('map', 'bản đồ'), ('guide', 'hướng dẫn viên'),
        ('airport', 'sân bay'), ('station', 'nhà ga'), ('taxi', 'xe taxi'), ('road', 'con đường'), ('journey', 'chuyến đi'),
        ('tourist', 'khách du lịch'), ('trip', 'chuyến du lịch'), ('visa', 'thị thực'), ('backpack', 'ba lô'), ('cruise', 'chuyến du thuyền'),
        ('ferry', 'phà'), ('subway', 'tàu điện ngầm'), ('departure', 'khởi hành'), ('arrival', 'đến nơi'), ('reservation', 'đặt chỗ')
    ],
    'School': [
        ('student', 'học sinh'), ('teacher', 'giáo viên'), ('class', 'lớp học'), ('lesson', 'bài học'), ('homework', 'bài tập về nhà'),
        ('exam', 'kỳ thi'), ('library', 'thư viện'), ('book', 'sách'), ('pencil', 'bút chì'), ('pen', 'bút mực'),
        ('notebook', 'vở'), ('desk', 'bàn học'), ('board', 'bảng'), ('subject', 'môn học'), ('math', 'toán'),
        ('science', 'khoa học'), ('history', 'lịch sử'), ('geography', 'địa lý'), ('biology', 'sinh học'), ('chemistry', 'hóa học'),
        ('grade', 'điểm số'), ('uniform', 'đồng phục'), ('recess', 'giờ ra chơi'), ('schedule', 'thời khóa biểu'), ('campus', 'khuôn viên trường')
    ],
    'Hobbies': [
        ('music', 'âm nhạc'), ('painting', 'vẽ tranh'), ('dancing', 'nhảy'), ('singing', 'hát'), ('reading', 'đọc'),
        ('writing', 'viết'), ('gardening', 'làm vườn'), ('cooking', 'nấu ăn'), ('fishing', 'câu cá'), ('hiking', 'đi bộ đường dài'),
        ('cycling', 'đạp xe'), ('swimming', 'bơi'), ('photography', 'nhiếp ảnh'), ('drawing', 'vẽ'), ('knitting', 'đan len'),
        ('gaming', 'chơi game'), ('traveling', 'du lịch'), ('movies', 'phim ảnh'), ('chess', 'cờ vua'), ('yoga', 'yoga'),
        ('jogging', 'chạy bộ'), ('baking', 'nướng bánh'), ('crafting', 'làm đồ thủ công'), ('surfing', 'lướt sóng'), ('collecting', 'sưu tầm')
    ],
    'Work': [
        ('office', 'văn phòng'), ('job', 'công việc'), ('career', 'sự nghiệp'), ('colleague', 'đồng nghiệp'), ('boss', 'sếp'),
        ('meeting', 'cuộc họp'), ('salary', 'lương'), ('project', 'dự án'), ('deadline', 'hạn chót'), ('resume', 'sơ yếu lý lịch'),
        ('interview', 'phỏng vấn'), ('skill', 'kỹ năng'), ('company', 'công ty'), ('worker', 'người lao động'), ('manager', 'quản lý'),
        ('schedule', 'lịch trình'), ('task', 'nhiệm vụ'), ('report', 'báo cáo'), ('contract', 'hợp đồng'), ('promotion', 'thăng chức'),
        ('break', 'giải lao'), ('team', 'nhóm'), ('overtime', 'làm thêm giờ'), ('training', 'đào tạo'), ('workplace', 'nơi làm việc')
    ],
    'Shopping': [
        ('store', 'cửa hàng'), ('market', 'chợ'), ('price', 'giá'), ('discount', 'giảm giá'), ('sale', 'đợt bán giảm'),
        ('cashier', 'thu ngân'), ('customer', 'khách hàng'), ('basket', 'giỏ'), ('cart', 'xe đẩy'), ('product', 'sản phẩm'),
        ('brand', 'thương hiệu'), ('quality', 'chất lượng'), ('receipt', 'hóa đơn'), ('exchange', 'đổi hàng'), ('refund', 'hoàn tiền'),
        ('size', 'kích cỡ'), ('color', 'màu sắc'), ('style', 'phong cách'), ('fashion', 'thời trang'), ('bargain', 'mặc cả'),
        ('shop', 'mua sắm'), ('mall', 'trung tâm thương mại'), ('fitting', 'phòng thử đồ'), ('delivery', 'giao hàng'), ('online', 'trực tuyến')
    ],
    'Health': [
        ('doctor', 'bác sĩ'), ('nurse', 'y tá'), ('hospital', 'bệnh viện'), ('clinic', 'phòng khám'), ('medicine', 'thuốc'),
        ('treatment', 'điều trị'), ('disease', 'bệnh'), ('symptom', 'triệu chứng'), ('vaccine', 'vắc xin'), ('exercise', 'tập thể dục'),
        ('diet', 'chế độ ăn'), ('stress', 'căng thẳng'), ('sleep', 'giấc ngủ'), ('injury', 'chấn thương'), ('pain', 'đau'),
        ('blood', 'máu'), ('heart', 'trái tim'), ('brain', 'não'), ('bone', 'xương'), ('muscle', 'cơ'),
        ('tooth', 'răng'), ('skin', 'da'), ('health', 'sức khỏe'), ('recovery', 'hồi phục'), ('checkup', 'kiểm tra sức khỏe')
    ],
    'Environment': [
        ('nature', 'thiên nhiên'), ('forest', 'rừng'), ('river', 'sông'), ('mountain', 'núi'), ('ocean', 'đại dương'),
        ('climate', 'khí hậu'), ('weather', 'thời tiết'), ('pollution', 'ô nhiễm'), ('recycle', 'tái chế'), ('waste', 'rác thải'),
        ('energy', 'năng lượng'), ('wildlife', 'động vật hoang dã'), ('conservation', 'bảo tồn'), ('planet', 'hành tinh'), ('earth', 'trái đất'),
        ('tree', 'cây'), ('air', 'không khí'), ('water', 'nước'), ('soil', 'đất'), ('ecosystem', 'hệ sinh thái'),
        ('habitat', 'môi trường sống'), ('species', 'loài'), ('global', 'toàn cầu'), ('warming', 'sự nóng lên'), ('sustainable', 'bền vững')
    ],
    'Technology': [
        ('computer', 'máy tính'), ('smartphone', 'điện thoại thông minh'), ('internet', 'mạng internet'), ('email', 'thư điện tử'), ('software', 'phần mềm'),
        ('hardware', 'phần cứng'), ('keyboard', 'bàn phím'), ('screen', 'màn hình'), ('mouse', 'chuột'), ('program', 'chương trình'),
        ('application', 'ứng dụng'), ('website', 'trang web'), ('network', 'mạng lưới'), ('password', 'mật khẩu'), ('data', 'dữ liệu'),
        ('cloud', 'đám mây'), ('digital', 'kỹ thuật số'), ('device', 'thiết bị'), ('battery', 'pin'), ('charger', 'bộ sạc'),
        ('camera', 'máy ảnh'), ('video', 'video'), ('audio', 'âm thanh'), ('download', 'tải xuống'), ('upload', 'tải lên')
    ],
    'Culture': [
        ('tradition', 'truyền thống'), ('festival', 'lễ hội'), ('music', 'âm nhạc'), ('art', 'nghệ thuật'), ('dance', 'múa'),
        ('language', 'ngôn ngữ'), ('custom', 'phong tục'), ('cuisine', 'ẩm thực'), ('heritage', 'di sản'), ('history', 'lịch sử'),
        ('literature', 'văn học'), ('religion', 'tôn giáo'), ('costume', 'trang phục'), ('celebration', 'lễ kỷ niệm'), ('ceremony', 'nghi lễ'),
        ('belief', 'niềm tin'), ('community', 'cộng đồng'), ('folklore', 'văn hóa dân gian'), ('myth', 'thần thoại'), ('theater', 'nhà hát'),
        ('sculpture', 'điêu khắc'), ('museum', 'bảo tàng'), ('poetry', 'thơ ca'), ('architecture', 'kiến trúc'), ('symbol', 'biểu tượng')
    ],
    'Weather': [
        ('sun', 'mặt trời'), ('rain', 'mưa'), ('cloud', 'mây'), ('wind', 'gió'), ('storm', 'bão'),
        ('snow', 'tuyết'), ('temperature', 'nhiệt độ'), ('forecast', 'dự báo'), ('season', 'mùa'), ('summer', 'mùa hè'),
        ('winter', 'mùa đông'), ('spring', 'mùa xuân'), ('autumn', 'mùa thu'), ('climate', 'khí hậu'), ('humidity', 'độ ẩm'),
        ('thunder', 'sấm'), ('lightning', 'tia chớp'), ('hail', 'mưa đá'), ('breeze', 'gió nhẹ'), ('fog', 'sương mù'),
        ('drought', 'hạn hán'), ('flood', 'lũ lụt'), ('rainbow', 'cầu vồng'), ('sunshine', 'ánh nắng'), ('frost', 'sương giá')
    ],
    'Sports': [
        ('soccer', 'bóng đá'), ('basketball', 'bóng rổ'), ('tennis', 'quần vợt'), ('baseball', 'bóng chày'), ('volleyball', 'bóng chuyền'),
        ('golf', 'gôn'), ('running', 'chạy bộ'), ('swimming', 'bơi lội'), ('cycling', 'đạp xe'), ('boxing', 'đấm bốc'),
        ('stadium', 'sân vận động'), ('coach', 'huấn luyện viên'), ('player', 'cầu thủ'), ('team', 'đội'), ('match', 'trận đấu'),
        ('referee', 'trọng tài'), ('score', 'tỷ số'), ('goal', 'bàn thắng'), ('medal', 'huy chương'), ('athlete', 'vận động viên'),
        ('training', 'luyện tập'), ('competition', 'thi đấu'), ('victory', 'chiến thắng'), ('defeat', 'thất bại'), ('league', 'giải đấu')
    ],
    'Home': [
        ('house', 'ngôi nhà'), ('apartment', 'căn hộ'), ('kitchen', 'nhà bếp'), ('bathroom', 'phòng tắm'), ('bedroom', 'phòng ngủ'),
        ('livingroom', 'phòng khách'), ('window', 'cửa sổ'), ('door', 'cửa'), ('furniture', 'đồ nội thất'), ('sofa', 'ghế sofa'),
        ('bed', 'giường'), ('table', 'bàn'), ('chair', 'ghế'), ('lamp', 'đèn'), ('floor', 'sàn'),
        ('ceiling', 'trần nhà'), ('wall', 'tường'), ('garden', 'vườn'), ('garage', 'ga ra'), ('roof', 'mái nhà'),
        ('yard', 'sân'), ('fence', 'hàng rào'), ('hallway', 'hành lang'), ('stairs', 'cầu thang'), ('basement', 'tầng hầm')
    ],
    'Transportation': [
        ('road', 'con đường'), ('street', 'đường phố'), ('highway', 'cao tốc'), ('traffic', 'giao thông'), ('lane', 'làn đường'),
        ('bike', 'xe đạp'), ('car', 'xe hơi'), ('bus', 'xe buýt'), ('train', 'tàu hỏa'), ('subway', 'tàu điện ngầm'),
        ('station', 'ga'), ('stop', 'điểm dừng'), ('ticket', 'vé'), ('fare', 'tiền vé'), ('driver', 'tài xế'),
        ('passenger', 'hành khách'), ('route', 'tuyến đường'), ('schedule', 'lịch trình'), ('taxi', 'xe taxi'), ('parking', 'bãi đậu xe'),
        ('bridge', 'cầu'), ('tunnel', 'đường hầm'), ('ferry', 'phà'), ('airport', 'sân bay'), ('vehicle', 'phương tiện')
    ],
    'Nature': [
        ('tree', 'cây'), ('flower', 'hoa'), ('grass', 'cỏ'), ('leaf', 'lá'), ('seed', 'hạt'),
        ('root', 'rễ'), ('soil', 'đất'), ('rock', 'đá'), ('river', 'sông'), ('lake', 'hồ'),
        ('mountain', 'núi'), ('valley', 'thung lũng'), ('forest', 'rừng'), ('desert', 'sa mạc'), ('beach', 'bãi biển'),
        ('island', 'đảo'), ('ocean', 'đại dương'), ('sky', 'bầu trời'), ('star', 'ngôi sao'), ('moon', 'mặt trăng'),
        ('sun', 'mặt trời'), ('cloud', 'mây'), ('rain', 'mưa'), ('wind', 'gió'), ('animal', 'động vật')
    ],
    'Time': [
        ('morning', 'buổi sáng'), ('afternoon', 'buổi chiều'), ('evening', 'buổi tối'), ('night', 'ban đêm'), ('day', 'ngày'),
        ('week', 'tuần'), ('month', 'tháng'), ('year', 'năm'), ('today', 'hôm nay'), ('tomorrow', 'ngày mai'),
        ('yesterday', 'hôm qua'), ('calendar', 'lịch'), ('clock', 'đồng hồ'), ('minute', 'phút'), ('hour', 'giờ'),
        ('second', 'giây'), ('schedule', 'lịch trình'), ('deadline', 'hạn chót'), ('past', 'quá khứ'), ('present', 'hiện tại'),
        ('future', 'tương lai'), ('soon', 'sớm'), ('late', 'muộn'), ('early', 'sớm'), ('season', 'mùa')
    ],
    'Emotions': [
        ('happy', 'hạnh phúc'), ('sad', 'buồn'), ('angry', 'tức giận'), ('afraid', 'sợ hãi'), ('surprised', 'ngạc nhiên'),
        ('tired', 'mệt mỏi'), ('excited', 'háo hức'), ('bored', 'chán'), ('nervous', 'lo lắng'), ('calm', 'bình tĩnh'),
        ('proud', 'tự hào'), ('ashamed', 'xấu hổ'), ('worried', 'lo âu'), ('hopeful', 'hy vọng'), ('lonely', 'cô đơn'),
        ('relaxed', 'thư giãn'), ('scared', 'sợ'), ('jealous', 'ghen tị'), ('grateful', 'biết ơn'), ('hungry', 'đói'),
        ('thirsty', 'khát'), ('satisfied', 'hài lòng'), ('frustrated', 'bực bội'), ('curious', 'tò mò'), ('confident', 'tự tin')
    ]
}

# Example templates for each topic
example_templates = {
    'Family': 'My {} is kind.',
    'Food': 'I eat {} every day.',
    'Travel': 'We need a {} when we travel.',
    'School': 'The {} is in the classroom.',
    'Hobbies': 'I enjoy {} in my free time.',
    'Work': 'My {} is very important at work.',
    'Shopping': 'This {} is useful when shopping.',
    'Health': 'The {} helps my health.',
    'Environment': 'Protect the {} for the future.',
    'Technology': 'The {} is a common device.',
    'Culture': '{} is part of our culture.',
    'Weather': 'Today the {} is strong.',
    'Sports': '{} is a popular sport.',
    'Home': 'The {} is in my house.',
    'Transportation': 'The {} is on the road.',
    'Nature': 'The {} is in nature.',
    'Time': '{} passes quickly.',
    'Emotions': 'Sometimes I feel {}.'
}

# Video links per topic (placeholders)
video_links = {
    'Family': 'https://www.youtube.com/watch?v=3vhLb8h6eJg',
    'Food': 'https://www.youtube.com/watch?v=4V86xHzqS8c',
    'Travel': 'https://www.youtube.com/watch?v=5YQoF-nN-3c',
    'School': 'https://www.youtube.com/watch?v=6Zs5wu-LE2o',
    'Hobbies': 'https://www.youtube.com/watch?v=7aM4u_GagWc',
    'Work': 'https://www.youtube.com/watch?v=8bL1sV1qh7s',
    'Shopping': 'https://www.youtube.com/watch?v=9cN7eUe3rD8',
    'Health': 'https://www.youtube.com/watch?v=AdE4w_xFe2E',
    'Environment': 'https://www.youtube.com/watch?v=BfF6q1Wz1sE',
    'Technology': 'https://www.youtube.com/watch?v=CgG8iQ7pI-k',
    'Culture': 'https://www.youtube.com/watch?v=DhH1k8yN2RM',
    'Weather': 'https://www.youtube.com/watch?v=EkK2t9xLzVU',
    'Sports': 'https://www.youtube.com/watch?v=FlL3e1M3pYQ',
    'Home': 'https://www.youtube.com/watch?v=GmM4f2N5r5s',
    'Transportation': 'https://www.youtube.com/watch?v=HnN5g3O6t6U',
    'Nature': 'https://www.youtube.com/watch?v=IpO6h4P7u7Y',
    'Time': 'https://www.youtube.com/watch?v=JqP7i5Q8v8Z',
    'Emotions': 'https://www.youtube.com/watch?v=KrQ8j6R9w9A'
}

plan = []
day = 1
for topic, words in vocab_data.items():
    video = video_links.get(topic, '')
    template = example_templates.get(topic, 'Example sentence with {}.')
    for i in range(0, len(words), 5):
        vocab_list = []
        for word, trans in words[i:i+5]:
            w = word.capitalize() if topic in {'Culture', 'Sports', 'Time'} else word
            example = template.format(w)
            vocab_list.append({'word': word, 'translation': trans, 'example': example})
        entry = {
            'day': day,
            'topic': topic,
            'vocabulary': vocab_list,
            'video': video,
            'speaking': 'Shadow the video and talk about the topic for 5 sentences.',
            'writing': 'Write 3-5 sentences about your day using today\'s vocabulary.'
        }
        if day > 45:
            entry['ielts'] = 'Do one IELTS practice task (listening or reading) from Cambridge book.'
        plan.append(entry)
        day += 1

with open('data/90_day_plan.json', 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

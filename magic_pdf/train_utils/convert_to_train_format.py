

def convert_to_train_format(jso: dict) -> []:
    pages = []
    for k, v in jso.items():
        page_idx = v["page_idx"]
        width, height = v["page_size"]

        info = {"page_info": {"page_no": page_idx, "height": height, "width": width}}

        bboxes: list[dict] = []
        for img_bbox in v["image_bboxes_with_caption"]:
            bbox = {"category_id": 1, "bbox": img_bbox["bbox"]}
            if "caption" in img_bbox:
                bbox["caption_bbox"] = img_bbox["caption"]
            bboxes.append(bbox)

        for tbl_bbox in v["table_bboxes_with_caption"]:
            bbox = {"category_id": 7, "bbox": tbl_bbox["bbox"]}
            if "caption" in tbl_bbox:
                bbox["caption_bbox"] = tbl_bbox["caption"]
            bboxes.append(bbox)

        for bbox in v["bak_page_no_bboxes"]:
            n_bbox = {"category_id": 4, "bbox": bbox}
            bboxes.append(n_bbox)

        for bbox in v["bak_header_bboxes"]:
            n_bbox = {"category_id": 3, "bbox": bbox}
            bboxes.append(n_bbox)

        for bbox in v["bak_footer_bboxes"]:
            n_bbox = {"category_id": 6, "bbox": bbox}
            bboxes.append(n_bbox)

        # 脚注， 目前没有看到例子
        for para in v["para_blocks"]:
            n_bbox = {"category_id": 2, "bbox": para["bbox"]}
            bboxes.append(n_bbox)

        for inline_equation in v["inline_equations"]:
            n_bbox = {"category_id": 13, "bbox": inline_equation["bbox"]}
            bboxes.append(n_bbox)

        for inter_equation in v["interline_equations"]:
            n_bbox = {"category_id": 10, "bbox": inter_equation["bbox"]}
            bboxes.append(n_bbox)

        info["bboxes"] = bboxes
        pages.append(info)

    return pages
